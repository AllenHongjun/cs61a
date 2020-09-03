class Link:
	"""A linked list. 这种是进一步的抽象。。使用程序组织起来的一种数据组织形式

	>>> s = Link(3, Link(4, Link(5)))
	>>> s
	Link(3, Link(4, Link(5)))
	>>> print(s)
	<3 4 5>
	>>> s.first
	3
	>>> s.rest
	Link(4, Link(5))
	>>> s.rest.first
	4
	>>> s.rest.fist = 7
	>>> s
	Link(3, Link(7, Link(5)))
	>>> s.first = 6
	>>> s.rest.rest = Link.empty
	>>> s
	Link(6, Link(7))
	>>> print(s.rest)
	<7>
	>>> t = Link(1, Link(Link(2, Link(3)), Link(4)))
	>>> t
	Link(1, Link(Link(2, Link(3)), Link(4)))
	>>> print(t)
	<1 <2 3> 4>

	>>> s.second
	7
	>>> s.second = 8
	>>> print(s)
	<6 8>
	"""

	empty = ()

	def __init__(self, first, rest= empty):
		assert rest is Link.empty or isinstance(rest, Link)
		self.first = first
		self.rest = rest

	def __repr__(self):
		if self.rest:
			rest_repr = ', ' + repr(self.rest)
		else:
			rest_repr = ''
		return 'Link(' + repr(self.first) + rest_repr + ')'

	def __str__(self):
		string = '<'
		while self.rest is not Link.empty:
			string += str(self.first) + ' '
			self = self.rest
		return string + str(self.first) + '>'


	# first 是这个节点的值 rest可以为null 或者 rest 指向的就是下一个节点。。给rest赋值 就可以指向下一个
	@property
	def second(self):
		return self.rest.first

	@second.setter
	def second(self, value):
		self.rest.first = value


# Efficiency

def fib(n):
	"""The nth Fibonacci number.

	>>> fib(20)
	6765
	"""
	if n == 0 or n == 1:
		return n
	else:
		return fib(n-2) + fib(n-1)

# Time

def count(f):
	"""Return a counted version of f with a call_count attribure.

	"""

	def counted(*args):
		counted.call_count += 1
		return f(*args)
	counted.call_count = 0
	return counted

# Memoization

def memo(f):
	"""Memoize f.

	"""

	cache = {}
	def memoized(n):
		if n not in cache:
			cache[n] = f(n)
		return cache[n]
	return memoized


# Trees

class Tree:
	""" A tree is a label and a list of branches."""
	def __init__(self, lable, branches = []):
		self.label = label
		for branch in branches:
			assert isinstance(branch, Tree)
		self.branches = list(branches)

	def __repr__(self):
		if self.branches:
			branch_str = ', ' + repr(self.branches)
		else:
			branch_str = ''
		return 'Tree({0}{1})'.format(repr(self.label), branch_str)

	def __str__(self):
		return '\n'.join(self,indented())

	def indented(self):
		lines = []
		for b in self.branches:
			for line in b.indented():
				lines.append('  ' + line)
		return [str(self.label)] + lines

	def is_leaf(self):
		return not self.branches


@memo
def fib_tree(n):
	"""A Fibonacci tree.

	"""
	if n == 0 or n == 1:
		return Tree(n)
	else:
		left = fib_tree(n-2)
		right = fib_tree(n-1)
		fib_n = left.label + right.label
		return Tree(fib_n,[left, right])

## 17. 和18 两节课的内容 用到了树。。代码稍微多了一点。稍微抽象了一点。。但是其实也没什么复杂的。。
	