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


