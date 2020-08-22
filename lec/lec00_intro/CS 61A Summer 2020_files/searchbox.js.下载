const limit = 5;

const inputField = document.querySelector(".searchbox input");
const results = document.querySelector(".searchResults");
const moreButton = document.querySelector(".searchbox ul");

const headers = ["Resource", "Type", "Tags"];

const search = async (query, limit) => {
    if (limit <= 0) {
        return [];
    }
    const genericParams = {
        from: 0,
        size: (limit === Infinity ? 100 : limit),
        query: {
            multi_match: {
                query,
                type: "bool_prefix",
                fields: ["name", "tags^8", "type^6", "content"],
                fuzziness: "AUTO"
            },
        },
        highlight: {
            fields: {
                name: { number_of_fragments: 0 },
                tags: { number_of_fragments: 0 },
                type: { number_of_fragments: 0 },
                content: {},
            },
            order: "score",
        },
    };

    const params = {
        piazza_params: genericParams,
        resource_params: genericParams,
    };

    const { piazza, resources } = await (await fetch("https://61a-search.app.cs61a.org/query", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(params)
    })).json();

    const results = [].concat(resources.hits.hits, piazza.hits.hits).sort((a, b) => b._score - a._score);

    return results.map(({ _source: { name, display, type, link, tags }, highlight }) => {
        const bestHighlight = Object.fromEntries(Object.entries(highlight || {}).map(([k, v]) => [k, v[0]]));
        const displayName = display || name;
        if (displayName.includes("<a")) {
            return [displayName, type, tags.join(", "), bestHighlight.content];
        } else {
            const wrapper = document.createElement("div");
            const a = document.createElement("a");
            a.href = link;
            a.innerHTML = displayName;
            wrapper.appendChild(a);
            return [wrapper.innerHTML, type, tags.join(", "), bestHighlight.content];
        }
    }).slice(0, limit);
};

const updateTable = (rows, isMore) => {
    results.innerHTML = "";
    if (rows.length !== 0) {
        const table = document.createElement("table");
        table.classList.add("table", "table-hover");
        const tableHeader = document.createElement("thead");
        const headerRow = document.createElement("tr");
        for (const header of headers) {
            const headerElem = document.createElement("th");
            headerElem.textContent = header;
            headerRow.appendChild(headerElem);
        }
        tableHeader.appendChild(headerRow);
        table.appendChild(tableHeader);

        const tableBody = document.createElement("tbody");
        for (const row of rows) {
            const tableRow = document.createElement("tr");
            for (let i = 0; i !== headers.length; ++i) {
                const elem = document.createElement("td");
                elem.innerHTML = row[i];
                tableRow.appendChild(elem);
            }
            tableBody.appendChild(tableRow);
            if (row[3]) {
                const text = row[3].replace("<em>", "||em||").replace("</em>", "||notem||");
                const previewDiv = document.createElement("div");
                previewDiv.classList.add("preview");
                previewDiv.innerHTML = text;
                const stripped = previewDiv.innerText.trim();
                const emph = stripped.replace("||em||", "<em>").replace("||notem||", "</em>");
                previewDiv.innerHTML = emph;
                tableRow.children[0].appendChild(previewDiv);
            }
        }
        table.appendChild(tableBody);

        results.appendChild(table);
    }
    if (rows.length !== 0 && isMore) {
        moreButton.classList.remove("hidden");
    } else {
        moreButton.classList.add("hidden");
    }
};

const makeUpdater = (getAll) => async () => {
    const total = getAll ? Infinity : limit;
    const r1 = await search(inputField.value, total);
    updateTable(inputField.value && r1, !getAll);
};

inputField.addEventListener("input", makeUpdater(false));
moreButton.addEventListener("click", makeUpdater(true));
