# sumblie markdown markdown preview livereload 插件的使用
# 


# Generalizing patterns using arguments
from math import pi, sqrt

def area_square(r):
	"""Retrun the area of a square with side length R."""
	return r * r

def area_circle(r):
	"""Return the area of a circle with radius R."""
	return r * r * pi


def area_hexagon(r):
	"""Return the area of a regular hexagon with side lengt R."""
	return r * r * 3 * sqrt(3) / 2

def area(r, shape_constant):
	## 所谓的抄代码 其实不是只是抄写
	## 而是认真的阅读和理解一般
	## 然后也能更加熟练的使用工具。。方便调试
	"""Return the area of a shape from length measurement R."""
	assert r > 0, 'A length must be positive'
	return r * r * shape_constant



def area_square(r):
	return area(r, 1)

def area_circle(r):
	return area(r, pi)

def area_hexagon(r):
	return area(r, 3 * sqrt(3) / 3)



# Function as arguments

def sum_naturals(n):
	## 从1累加到 n 注意这里使用 <= 这样就比较的好理解
	"""Sum the first N natural numbers.

	>>> sum_naturals(5)
	15
	"""
	total, k = 0, 1
	while k <= n:
		total, k = total + k, k + 1
	return total

def sum_cubes(n):
	## 累加的使用 注意这个公因子一样的符号的表示 k, pow(k , 3) + k * k
	## 这些就很好理解
	## 初等数学的知识体系是没是样子的。。一个概括的知识结构。。
	"""Sum the first N cubes of natural numbers.

	>>> sum_cubes(5)
	225
	"""
	total, k = 0, 1
	while k <= n:
		total, k = total + pow(k, 3), k + 1

def identity(k):
	return k

def cube(k):
	return pow(k, 3)

def summation(n, term):
	##公共的地方使用一个函数来表示。。大大的减少开发的代码
	## 提取作为一个公共的函数 看起来麻烦。。其实不难 也是值得做的
	## 添加注释最后不要随意。。考虑到以后会阅读。注意格式
	## 认真的安静的坐下来。。敲10分钟代码。心态真的就放平了。
	"""Sum the first N terms of a sequence.

	>>> summation(5, cube)
	225
	"""
	total, k = 0, 1
	while k <= n:
		total = total + term(k), k + 1
	return total


from operator import mul

def pi_term(k):
	return 8 / mul(k * 4 -3, k * 4 -1)

#summation(1000000, pi_term)


#Local function definitaions ; returning functions

def make_adder(n):
	"""Return a function that takes one argument K and returns K + N.

	>>> add_three = make_adder(3)
	>>> add_three(4)
	7
	"""
	def adder(k):
		return k + n
	return adder

make_adder(2000)(19)


# Example: Sound

from wave import open
from struct import Struct
from math import floor

frame_rate = 11025

def encode(x):
	"""Encode float x between -1 and 1 as two bytes.
	"""
	i = int(16384 * x)
	return Struct('h').pack(i)

def play(sampler, name='song.wav', seconds=2):
	"""Write the output of a sampler function as a wav file.
	"""
	out = open(name, 'wb')
	out.setnchannels(1)
	out.setsampwidth(2)
	out.setframerate(frame_rate)
	t = 0
	while t < seconds * frame_rate:
		sample = sampler(t)
		out.writeframes(encode(sample))
		t = t + 1
	out.close()

def tri(frequency, amplitude=0.3):
	"""A continuous triangle wave."""
	period = frame_rate // frequency
	def sampler(t):
		saw_wave = t / period - floor(t / period + 0.5)
		tri_wave = 2 * abs(2 * saw_wave) - 1
		return amplitude * tri_wave
	return sampler

c_freq, e_freq, g_freq = 261.63, 329.63, 392.00

## 函数作为一个参数。。函数的返回值作为一个函数的参数
play(tri(e_freq))


def note(f, start, end, fade = .01):
	"""Play f for a fixed duration."""
	def sampler(t):
		seconds = t / frame_rate
		if seconds < start:
			return 0
		elif seconds > end:
			return 0
		elif seconds < start + fade:
			return (seconds - start) / fade * f(t)
		elif seconds > end - fade:
			return (end - seconds) / fade * f(t)
		else:
			return f(t)
	return sampler

play(note(tri(e_freq), 1, 1.5))

def both(f, g):
	return lambda t: f(t) + g(t)

c = tri(c_freq)
e = tri(e_freq)
g = tri(g_freq)
low_g = tri(g_freq / 2)

play(both(note(e, 0, 1/8), note(low_g, 1/8, 3/8)))


## 自带处理生成音乐的类库。。web 请求的模块。。 各种模块加载非常的方便
#play(both(note(c, 0, 1), both(note(e, 0, 1), note(g, 0, 1)) ))


def mario(c, e, g, low_g):
	z = 0
	song = note(e, z, z + 1/8)
	z += 1/8
	song = both(song, note(e, z, z + 1/8))
	z += 1/4
	song = both(song, note(e, z, z + 1/8))
	z += 1/4
	song = both(song, note(c, z, z + 1/8))
	z += 1/8
	song = both(song, note(e, z, z + 1/8))
	z += 1/4
	song = both(song, note(g, z, z + 1/4))
	z += 1/2
	song = both(song, note(low_g, z, z + 1/4))
	return song

def mario_at(octive):
	c = tri(octive * c_freq)
	e = tri(octive * e_freq)
	g = tri(octive * g_freq)
	low_g = tri(octive * g_freq / 2)
	return mario(c, e, g, low_g)

play(both(mario_at(1), mario_at(1/2)))



def square(x):
	return x * x

# Composition
## 区别函数的定义 函数的嵌套定义 函数左边一个变量赋值 函数的调用

def compose1(f, g):
	"""Return a function that composes f and g.

	f, g -- functions of a single argument
	"""
	def h(x):
		return f(g(x))
	return h

def triple(x):
	return 3 * x

squiple = compose1(square, triple)


def curry2(f):
	## 函数嵌套定义其中。然后返回一个函数的名称
	"""Curry a two-argument function.

	>>> m = curry2(add)
	>>> add_three = m(3)
	>>> add_three(4)
	7
	>>> m(2)(1)
	3
	"""
	def g(x):
		def h(y):
			return f(x, y)
		return h
	return g
