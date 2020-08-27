def iterator_demos():
	"""Using iterators

	>>> s = [[1, 2], 3, 4, 5]
	>>> next(s)
	Traceback (most recent call last):
		...
	TypeError: 'list' object is not an iterator

	>>> t = iter(s)
	>>> next(t)
	[1, 2]
	>>> next(t)
	3
	>>> u = iter(s)
	>>> next(u)
	[1, 2]


	"""


def plus_minux(x):
	"""Yield x and -x

	"""
	yield x
	yield -x

def evens(start, end):
	"""A generator funciton that returns even numbers.

	"""
	even = start + (start % 2)
	while even < end:
		yield even
		even += 2

class Countdown:

	def __init__(self, start):
		self.start = start

	def __iter__(self):
		v = self.start
		while  v > 0:
			yield v
			v -= 1

def a_then_b_for(a, b):
	for x in a:
		yield x
	for x in b:
		yield x

def a_then_b(a, b):
	yield from a
	yield from b


def countdown(k):

	if k > 0:
		yield k
		yield from countdown(k - 1)

def prefixes(s):

	if s:
		yield from prefixes(s[:-1])
		yield s

def substrings(s):

	if s:
		yield from prefixes(s)
		yield from substrings(s[1:])