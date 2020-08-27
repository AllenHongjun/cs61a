# Lists

odds = [41, 43, 47, 49]
len(odds)
odds[1]
odds[0] - odds[3] + len(odds)
odds[odds[3] - odds[2]]

# Containers

digits = [1, 8, 2, 8]
1 in digits
'1' in digits
[1, 8] in digits
[1, 2] in digits

# For statments

def count_while(s, value):
	"""Count the number of occurrences of value in sequence s.  在序列s中计算 value出现的次数

	>>> count_while(digits, 8)
	2
	"""
	total, index = 0, 0
	while index < len(s):
		if s[index] == value:
			total = total + 1
		index = index + 1
	return total

def count_for(s, value):
	"""Count the number of occurrences of value in sequence s.

	>>> count_for(digits, 8)
	2
	"""
	total = 0
	for elem in s:
		if elem == value:
			total = total + 1
	return total

def count_same(pairs):
	"""Return how many pairs have the same element repeated.

	>>> pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]
	>>> count_same[pairs]
	2
	"""
	same_count = 0
	for x, y in pairs:
		if x == y:
			same_count = same_count + 1
	return same_count


# Ranges

def sum_below(n):
	total = 0
	for i in range(n):
		total += i
	return total

def cheer():
	for _ in range(3):
		print('Go Bears!')

# List comprehensions

## Go Bears! 雄起 熊起
## 有很多时候 运行一下结果。。都不要看语法的解释就能大概明白这个写法是什么意思

odds = [1, 3, 5, 7, 9]
[x+1 for x in odds]
#[2, 4, 6, 8, 10]
[x for x in odds if 25 % x == 0]
#[1, 5]

# Rational arithmetic

def add_rational(x, y):
	"""The sum of rational numbers X and Y."""
	nx, dx = number(x), denom(x)
	ny, dy = number(x), denom(y)
	return rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
	"""The product of rational numbers X and Y. """
	return rational(number(x) * number(y), denom(x) * denom(y))

def rationals_are_equal(x, y):

	"""True iff rational numbers X and Y are equal."""
	return number(x) * denom(y) == number(y) * denom(x)


#....  这一块的内容需要学习一下 课件 和 视频。。是不了解的知识


# Dicts

def dict_demos():
	numerals = {'I':1, 'V':5, 'X':10}
	numerals['X']
	numerals.values()
	list(numerals.values())
	sum(numerals.values())
	dict([(3, 9), (4, 16), (5, 25)])
	numerals.get('X', 0)
	numerals.get('X-ray', 0)
	{x: x*x for x in range(3,6)}

	{1:2, 1:3}
	{[1]:2}
	{1:[2]}