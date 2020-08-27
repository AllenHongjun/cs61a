
## 看了代码 在看看课件。。之前不了解的 迭代器。。产生器。。概念有有了。。yeild  与 async  异步不是一个东西。

def date_demo():
	from datetime import datetime
	today = date(2018, 9, 21)
	freedom = date(2015, 12, 12)
	str(freedom - today)
	today.year
	today.strftime('%A, %B, %d')
	type(today)

def string_demos():
	hex(ord('A'))
	print('\a')
	print('1\n2\n3')
	from unicodedata import lookup, name
	name('A')
	lookup('SNOWMAN')
	lookup('SOCCER BALL')
	lookup('BABY')
	s = lookup('SNOWMAN')
	len('A')
	'A'.encode()
	len(frown)
	len(frown.encode())
	dir('')
	'hello'.capitalize()
	"hello".upper()

## 长链接其实也没有什么的。。就是调用一个方法。。可以发送请求

def list_demos():
	suits = ['coin', 'string', 'myriad']
	original_suits = suits
	suits.pop()
	suits.remove('string')
	suits.append('cup')
	suits.extend(['sword', 'club'])
	suits[2] = 'spade'
	suits
	suits[0:2] = ['heart', 'diamond']
	[suit.upper() for suit in suits]
	[suit[1:4] for suit in suits if len(suit) == 5]

def dict_demos():
	numerals = {'I' : 1.0,'V' : 5,'X' : 10 }
	numerals['X']
	numerals['I'] = 1
	numerals['L'] = 50
	numerals
	sum(numerals.values())
	dict([(3, 9), (4, 16), (5, 25)] )
	numerals.get('A', 0)
	numerals.get('V', 0)

def tuple_demos():
	(3, 4, 5, 6)
	3, 4, 5, 6
	()
	tuple()
	tuple([1, 2, 3])
	(2,)
	(3, 4) + (5, 6)
	(3, 4, 5) * 2
	5 in (3, 4 ,5)

	{1 : [2]}
	{(1, 2) : 3}
	{tuple([1, 2]) : 3}

def divide_exact(n, d):
	return n // d, n % d

def identity_demos():
	a = [10]
	b = a
	a == b
	a is b
	a.extend([20, 30])
	a == b
	a is b

	a = [10]
	b = [10]
	a == b
	a is not b
	a.append(20)
	a != b