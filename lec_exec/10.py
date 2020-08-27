# Slicing
odds = [3, 5, 7, 9, 11]
list(range(1,3))
[odds[i] for i in range(1,3)]
odds[1:3]
odds[1:]
odds[:3]
odds[:]

# Aggregation
sum(odds)
sum({3:9, 5:25})
max(range(10))
max(range(10),key = lambda x: 7 - (x-2)*(x-4))
all([x < 5 for x in range(5)])
perfect_square = lambda x:x == round(x ** 0.5) ** 2
any([perfect_square(x) for x in range(50, 60)])

# Trees

def tree(label, branches[]):
	for branch in branches:
		assert is_tree(branch), 'branches must be trees'
	return [label] + list(branches)

def label(tree):
	return tree[0]

def branches(tree):
	return tree[1:]

def is_tree(tree):
	if type(tree) != list or len(tree) < 1:
		return False
	for branch in branches(tree):
		if not is_tree(branch):
			return False
	return True

def is_leaf(tree):
	return not branches(tree)


### +++ === abstraction barrirer === ++++ ###

def fib_tree(n):
	"""Contruct a Fibonacci tree.

	>>> fib_tree(1)
	[1]
	>>> fib_tree(3)
	[2, [1], [1, [0], [1]]]

	"""
	if n == 0 or n== 1:
		return tree(n)
	else:
		left = fib_tree(n - 2)
		right = fib_tree(n - 1)
		fib_n = label(left) + label(right)
		return tree(fib_n, [left, right])

def count_leaves(t):
	"""The number of leaves in tree.

	>>> count_leaves(fib_tree(5))
	8
	"""
	if is_leaf(t):
		return 1
	else:
		return sum([count_leaves(b) for b in branches(t)])

def leaves(tree):
	"""Return a list containing the leaf labels of tree.

	>>> leaves(fib_tree(5))
	[1, 0, 1, 0, 1, 1, 0, 1]
	"""
	if is_leaf(tree):
		return [label(tree)]
	else:
		return sum([leaves(b) for b in branches(tree)],[])

def print_tree(t, indent=0):

	print('  ' * indent + str(label(t)))
	for b in branches(t):
		print_tree(b, indent + 1)

def increment_leaves(t):
	if is_leaf(t):
		return tree(label(t) + 1)
	else:
		bs = [increment_leaves(b) for b in branches(t)]
		return tree(label(t),bs)

def increment(t):
	return tree(label(t) + 1, [increment(b) for b in branches(t)])