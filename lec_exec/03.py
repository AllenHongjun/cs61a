from operator import truediv, floordiv,mod
# Dostrings, doctest, & default arguments
## python3 -i 03.py    python3 -m doctest 03.py
## IndentationError: unindent does not match any outer indentation level  缩进的问题
def divide_exact(n, d = 10):
	"""Return the quotient and remainder of dividing N by D.

	>>> quotient, remainder = divide_exact(618,10)
	>>> quotient
	61
	>>> remainder
	8
	"""
	return floordiv(n, d),mod(n, d)

# Conditional expressions
def absolute_value(x):
	"""Return the absolute value of x.

	>>> absolute_value(-2)
	2
	>>> absolute_value(0)
	0
	>>> absolute_value(3)
	3
	"""
	if x < 0:
		return -x
	elif x == 0:
		return 0
	else:
		return x

# Summation via while
## 编码规范需要注意一下 
## 操作符号两边需要有缩进
## 这些基本的代码 需要非常的熟悉
## 直接就能够敲出来。。
## 我是比较笨的人。。就多看代码 多看例子
# 调试运行代码 第一遍先抄一遍。然后做作业
## 能够举一反三 灵活运用就可以。。
## 也不要求自己能够创造出什么新的算法
## 新的解题思路。。
i, total = 0, 0
while i < 10:
	#print('i: ',i,'total: ',total)
	i = i + 1
	total = total + i
	#print('+++++++++++++++++++++')
	#print('i: ',i,'total: ',total)
total

def end(n, d):
	"""Print the final digits of N in revierse order until D is found.
	倒叙打印n的数字 直到d这个数字被找到

	>>> end(234324,3)
	4
	2
	3
	"""
	while n > 0:
		last, n = n % 10, n // 10
		### 先打印数字 ，如果答应的数字是最后一个数字就结束返回
		print(last)
		if d == last:
			return None




def is_three(x):
	"""Return whether x is three

	>>> search(is_three)
	3
	"""
	return x == 3



def positive(x):
	"""A function that is 0 until square(x) - 100 is positive

	>>> search(positive)
	11
	"""

	return max(0,square(x) - 100)


# 函数作为一个参数返回
def search(f):
	"""Return the smallest non-negative interger x for which f(x) is a true value."""
	x = 0
	while True:
		if f(x):
			return x
		x += 1


def square(x):
	return x * x

### doctest详细内容如何来显示
### lambda表达式如何理解
### 这个代码如何单不吊事如何运行
def invert(f):
	"""Return a function g(y) that returns x such that f(x) == y.

	>>> sqrt = invert(square)
	>>> sqrt(16)
	4
	"""
	return lambda y : search(lambda x : f(x) == y)


# Control
def if_(c, t, f):
	if c:
		t
	else:
		f

from math import sqrt

def real_sqrt(x):
	"""Return the real part of the square root of x.

	>>> real_sqrt(4)
	2.0
	>>> real_sqrt(-4)
	0.0
	"""
	if x > 0:
		return sqrt(x)
	else:
		return 0.0

def has_big_sqrt(x):
	"""Return whether x has a big square root.

	>>> has_big_sqrt(1000)
	True
	>>> has_big_sqrt(100)
	False
	>>> has_big_sqrt(0)
	False
	>>> has_big_sqrt(-1000)
	False
	"""
	return x > 0 and sqrt(x) > 10


def reasonable(n):
	"""Is N small enough that 1/N can be represented?

	>>> reasonable(100)
	True
	>>> reasonable(0)
	True
	>>> reasonable(-100)
	True
	>>> reasonable(10 ** 100)
	False
	"""

	return n == 0 or 1 / n != 0.0