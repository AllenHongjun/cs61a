# Functional arguments
def square(x):
	return x * x

def apply_twice(f, x):
	"""Return f(f(x))
	先执行f(x) . 然后将fx的返回值 带入f(x) 继续执行

	>>> apply_twice(square, 2)
	16
	>>> from math import sqrt
	>>> apply_twice(sqrt, 16)
	2.0
	"""
	return f(f(x))

result = apply_twice(square, 2)

# Functional return values

def make_adder(n):
	"""Return a function that takes one arguments k and returns k + n

	>>> add_three = make_adder(3)
	>>> add_three(4)
	7
	"""
	def adder(k):
		return k + n
	return adder

# Lexical scope and returning functions

def f(x, y):
	return g(x)

def g(a):
	return a + y

# Lambda expressions

x = 10
square = x * x
square = lambda x : x * x
print(square(4))


# Self Reference

def print_all(k):
	# 先执行这个函数。如何这个函数的返回值值函数自己本身或者还是一个函数。就会继续执行这个函数 一直到最后这个函数执行结束
	#f= func print_all(k) [parent=Global]

	"""Print all argument of repeated calls

	>>> f = print_all(1)(2)(3)(4)(5)
	1
	2
	3
	4
	5
	"""
	print(k)
	return print_all

f = print_all(1)(2)(3)(4)(5)

def print_sums(n):
	## 1. 定义一个父函数 和子函数 
	## 2. 父函数返回后子函数 子函数调用父函数。返回一个子函数
	## 3. 如果执行子函数。会调用父函数然后返回子函数
	## 4. 每一个括号是一次函数的调用（调用子函数是两次。因为会调用父函数、主要函数对象作为返回值）
	## 5. 子函数里面调用父级作用域。是有一个链表的树一样。
	## 递归的的如何要理解他一步一步的执行步骤还是有点累了
	## 如果只是看意思。。就好理解用地爱你
	## 6. 这些问题还都是可以单步调试来解决的。
	""" Print all sums of arguments of repeated calls

	>>> f = print_sums(1)(2)(3)(4)(5)
	1
	3
	6
	10
	15
	"""
	print(n)
	def next_sum(k):
		return print_sums(n + k)
	return next_sum

f = print_sums(1)(2)(3)(4)(5)