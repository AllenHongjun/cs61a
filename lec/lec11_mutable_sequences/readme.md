# mutable_sequence
## concepts
- Functions do one thing; objects do many related things
- Control characters were designed for transmission 空格 回车 换行。底层对应的ascii码也是一个二进制数字
- Only objects of mutable types can change: lists & dictionaries
- In Python, like many other programming languages, we use dot notation to designate an attribute of an object.
- Sharing and Identity. Because we have been changing a single list rather than creating new lists, the object bound to the name chinese has also changed, because it is the same list object that was bound to suits!
- Although the list is copied, the values contained within the list are not. Instead, a new list is constructed that contains a subset of the same values as the sliced list. Therefore, mutating a list within a sliced list will affect the original list.
- The append method of a list takes one value as an argument and adds it to the end of the list. 
- The extend method of a list takes an iterable value as an argument and adds each of its elements to the end of the list.
- The pop method removes and returns the last element of the list. When given an integer argument i, it removes and returns the element at index i of the list. 
- The remove method takes one argument that must be equal to a value in the list. It removes the first item in the list that is equal to its argument. Calling remove on a value that is not equal to any item in the list causes a ValueError.
- The index method takes one argument that must be equal to a value in the list. It returns the index in the list of the first item that is equal to the argument. 
- The insert method takes two arguments: an index and a value to be inserted. The value is added to the list at the given index.
- The count method of a list takes in an item as an argument and returns how many times an equal item apears in the list. If the argument is not equal to any element of the list, then count returns 0.

- While it is not possible to change which elements are in a tuple, it is possible to change the value of a mutable element contained within a tuple.
- The key to correctly analyzing code with non-local assignment is to remember that only function calls can introduce new frames. Assignment statements always change bindings in existing frames. In this case, unless make_withdraw is called twice, there can be only one binding for balance.

## questions

## idea
1. 英语和数学的学习当做一个爱好一样。最大的兴趣还是 计算机。
2. 第四周 是循环器 迭代器。。生成器。。对象 继承。链表 和树。。
3. 本周 第二章。。第一章内容 看了不少。。
4. 很多都是要自己做一个 ppt 来解释。。 ppt 文档。。这些的能力。。
5. google drive 

## new-words
- interactions
- first-class: in the best group; of the highest standard  一等的
- metaphor
- transmission：he act or process of passing sth from one person, place or thing to another 传送；传递；传达；传播；传染
- canonical：included in a list of holy books that are accepted as genuine; connected with works of literature that are highly respected
- scope:the range of things that a subject, an organization, an activity, etc. deals with （题目、组织、活动等的）范围
- vital 
- formulating 
- coherent 
- incorporate 
- ingredient :one of the things or qualities that are necessary to make sth successful
- paradigm:(technical 术语) a typical example or pattern of sth 典范；范例；样式
- Metaphor: a word or phrase used to describe sb/sth else, in a way that is different from its normal use, in order to show that the two things have the same qualities and to make the description more powerful, for example She has a heart of stone ; the use of such words and phrases 暗喻；隐喻
- terminology
- designate:~ sth (as) sth | ~ sth (as being sth) to say officially that sth has a particular character or name; to describe sth in a particular way 命名；指定
- Metaphorically
- facilitate 
- drastically 
- myriad
- comprehensions:[不可数名词] the ability to understand 理解力；领悟能力
- tuple:多元组泛指有限个元素所组成的序列。
- correspondence 
- consecutive : following one after another in a series, without interruption 连续不断的
- descriptive
- Intuitively
- analogous: similar in some way to another thing or situation and therefore able to be compared with it 相似的；类似的
- internal 
- autonomous 
- interact 
- nuances 
- subtleties 
- arbitrary 
- thorny 
- epistemological 
-  signal: movement or sound that you make to give sb information, instructions, a warning, etc. 信号；暗号
- unified 
- mechanism 
- Propagating 
- Constraints