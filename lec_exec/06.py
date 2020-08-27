# Sum digits

def split(n):
	"""Split a positive into all but its last digit and its last digit."""
	return n // 10, n % 10

def sum_digits(n):
	"""Return the sum of the digits of positive integer n.

	>>> sum_digits(9)
	9
	>>> sum_digits(18117)
	18
	>>> sum_digits(989283)
	33
	>>> sum_digits(11408855402054064613470328848384)
	126
	"""
	if n < 10:
		return n
	else:
		all_but_last, last = split(n)
		return sum_digits(all_but_last) + last

# Iteration vs recursion

def fact_iter(n):
	total, k = 1, 1
	while k <= n:
		total, k = total * k, k + 1
	return total

def fact(n):
	if n == 0:
		return 1
	else:
		return n * fact(n-1)

## 看起来复杂一点 。其实本质也也都是重复的调用一个函数
## 一直到满足退出的条件
# Luhn algorithm: mutual recursion

def luhn_sum(n):
	"""Return the digit sum of n computed by the Luhn algorithm.

	>>>luhn_sum(2)
	2
	>>> luhn_sum(12)
	4

	"""
	if n < 10:
		return n
	else:
		all_but_last, last = split(n)
		return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
	"""Return the Luhn sum of n, doubling the last digit."""
	all_but_last, last = split(n)
	luhn_digit = sum_digits(2 * last)
	if n < 10:
		return luhn_digit
	else:
		return luhn_sum(all_but_last) + luhn_digit

# Converting iteratoin to recursion

def sum_digits_iter(n):
	"""Sum digits iteratively.

	>>> sum_digits_iter(11408855402054064613470328848384)
	126
	"""
	digit_sum = 0
	while  n > 0:
		n, last = split(n)
		digit_sum = digit_sum + last
	return digit_sum

def sum_digits_rec(n, digit_sum):
	""" Sum digits using recursion, based on iterative version.

	>>> sum_digits_rec(11408855402054064613470328848384,0)
	126
	"""
	if n == 0:
		return digit_sum
	else:
		n, last = split(n)
		return sum_digits_rec(n, digit_sum + last)

# Ordering

## 先执行调用递归函数之前的内容。然后再执行递归函数之后的内容
## 瀑布
def cascade(n):
	"""Print a cascade of prefixes of n.

	>>> cascade(1234)
	1234
	123
	12
	1
	12
	123
	1234
	"""
	if n < 10:
		print(n)
	else:
		print(n)
		cascade(n//10)
		print(n)

## 先看书 看代码 看课件 自己理解一遍。。这个又不同的可以慢慢消化一下
## 找找资料 或者调试调试。

## 然后再听课。。不然直接听课。。第一遍肯定会有很多不懂。
## 会打击自信。。和打击积极性

## 自己看了一遍书再听。。会的可以巩固。。对不会的地方印象也会更加深刻
## 学习是最简单的一件事情了。。没有什么比学习更加简单了。

def cascade2(n):
	## 这个和上面的函数效果是一样的。但是更加简短。但是不好理解一点
	"""Print a cascade of prefixeds of n. """
	print(n)
	if n >= 10:
		cascade(n//10)
		print(n)


def inverse_cascade(n):
	"""Print an inverse cascade of prefixed of n.

	>>> inverse_cascade(1234)
	1
	12
	1234
	123
	12
	1
	"""
	grow(n)
	print(n)
	shrink(n)

def f_then_g(f, g, n):
	# 如果n>0就会一直执行
	# lambda表达式就是一个函数。但是写法更加的简洁一点
	if n:
		f(n)
		g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)