def str_repr_demos():
    from fractions import Fraction
    half = Fraction(1, 2)
    half
    print(half)
    str(half)
    repr(half)

    s = 'hello world'
    str(s)
    repr(s)
    "'hello world'"
    repr(repr(repr(s)))
    eval(eval(eval(repr(repr(repr(s))))))
    # Errors: eval('hello world')

# Implementing generic string functions

class Bear:
    """A Bear.


    >>> oski = Bear()
    >>> oski
    Bear()
    >>> print(oski)
    a bear
    >>> print(str(oski))
    a bear
    >>> print(repr(oski))
    Bear()
    >>> print(oski.__repr__())
    oski
    >>> print(oski.__str__())
    oski the bear

    >>> print(str_(oski))
    a bear
    >>> print(repr_(oski))
    Bear()
    """
    def __init__(self):
        self.__repr__ = lambda: 'oski' # instance attribute
        self.__str__ = lambda: 'oski the bear'

    def __repr__(self): # class attribute
        return 'Bear()'

    def __str__(self):
        return 'a bear'

def print_bear():
    oski = Bear()
    print(oski)
    print(str(oski))
    print(repr(oski))
    print(oski.__repr__())
    print(oski.__str__())

def repr_(x):
    s = type(x).__repr__(x)
    if not isinstance(s, str):
        raise TypeError
    return s

def str_(x):
    s = type(x).__str__(x)
    if not isinstance(s, str):
        raise TypeError
    return s

# Ratio numbers
from fractions import gcd

class Ratio:
    """A mutable ratio.

    >>> f = Ratio(9, 15)
    >>> f
    Ratio(9, 15)
    >>> print(f)
    9/15

    >>> Ratio(1, 3) + Ratio(1, 6)
    Ratio(1, 2)
    >>> f + 1
    Ratio(8, 5)
    >>> 1 + f
    Ratio(8, 5)
    >>> 1.4 + f
    2.0
    """
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)

    def __add__(self, other):
        if isinstance(other, Ratio):
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom
        elif isinstance(other, int):
            n = self.numer + self.denom * other
            d = self.denom
        else:
            return float(self) + other
        g = gcd(n, d)
        r = Ratio(n // g, d // g)
        return r

    __radd__ = __add__

    def __float__(self):
        return self.numer / self.denom

"Find something to eat"

import json
from ucb import main


def search(query, ranking=lambda r: -r.stars):
    """A restaurant search engine.

    >>> results = search("Thai")
    >>> results
    [<Thai Basil Cuisine>, <Thai Noodle II>, <Jasmine Thai>, <Berkeley Thai House>, <Viengvilay Thai Cuisine>]
    >>> for r in results:
    ...     print(r.name, 'shares reviewers with', r.similar(3))
    Thai Basil Cuisine shares reviewers with [<Gypsy's Trattoria Italiano>, <Top Dog>, <Smart Alec's Intelligent Food>]
    Thai Noodle II shares reviewers with [<La Cascada Taqueria>, <Cafe Milano>, <Chinese Express>]
    Jasmine Thai shares reviewers with [<Hummingbird Cafe>, <La Burrita 2>, <The Stuffed Inn>]
    Berkeley Thai House shares reviewers with [<Smart Alec's Intelligent Food>, <Thai Basil Cuisine>, <Top Dog>]
    Viengvilay Thai Cuisine shares reviewers with [<La Val's Pizza>, <Thai Basil Cuisine>, <La Burrita 2>]
    """
    results = [r for r in Restaurant.all if query in r.name]
    return sorted(results, key=ranking)


def num_shared_reviewers(restaurant, other):
    return fast_overlap(restaurant.reviewers, other.reviewers)
    return len([r for r in restaurant.reviewers if r in other.reviewers])


def fast_overlap(s, t):
    """Return the overlap between sorted S and sorted T.

    >>> fast_overlap([2, 3, 5, 6, 7], [1, 4, 5, 6, 7, 8])
    3
    """
    count, i, j = 0, 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            count, i, j = count + 1, i + 1, j + 1
        elif s[i] < t[j]:
            i += 1
        else:
            j += 1
    return count


class Restaurant:
    """A restaurant."""
    all = []
    def __init__(self, name, stars, reviewers):
        self.name = name
        self.stars = stars
        self.reviewers = reviewers
        Restaurant.all.append(self)

    def similar(self, k, similarity=num_shared_reviewers):
        "Return the K most similar restaurants to SELF, using SIMILARITY for comparison."
        others = list(Restaurant.all)
        others.remove(self)
        return sorted(others, key=lambda r: -similarity(self, r))[:k]

    def __repr__(self):
        return '<' + self.name + '>'


def load_reviews(reviews_file):
    reviewers_by_restaurant = {}
    for line in open(reviews_file):
        r = json.loads(line)
        business_id = r['business_id']
        if business_id not in reviewers_by_restaurant:
            reviewers_by_restaurant[business_id] = []
        reviewers_by_restaurant[business_id].append(r['user_id'])
    return reviewers_by_restaurant


def load_restaurants(reviewers_by_restaurant, restaurants_file):
    for line in open(restaurants_file):
        b = json.loads(line)
        reviewers = reviewers_by_restaurant.get(b['business_id'], [])
        Restaurant(b['name'], b['stars'], sorted(reviewers))


load_restaurants(load_reviews('reviews.json'), 'restaurants.json')
# Restaurant('Thai Basil', 3)
# Restaurant('Thai Delight', 3)
# Restaurant('Top Dog', 4)


@main
def run():
    search = SearchEngine()
    while True:
        print('>', end=' ')
        results = search.lookup(input().strip())
        for r in results:
            print(r.name, 'shares reviewers with', r.similar(3))
