# chapter2: building abstractins with data
# seqeunces and data abstraction

## questions
- 关于tree的代码 需要好好理解 和单步调试运行一下。。


## concept
- We concentrated in Chapter 1 on computational processes and on the role of functions in program design. We saw how to use primitive data (numbers) and primitive operations (arithmetic), how to form compound functions through composition and control, and how to create functional abstractions by giving names to processes. We also saw that higher-order functions enhance the power of our language by enabling us to manipulate, and thereby to reason, in terms of general methods of computation. This is much of the essence of programming.
- The built-in type function allows us to inspect the class of any value.
- [10 Best Python Books 2020](https://finderiko.com/python-book)
- One intuition that supports this indexing convention is that the index represents how far an element is offset from the beginning of the list.
- Any values can be included in a list, including another list. Element selection can be applied multiple times in order to select a deeply nested element in a list containing lists.
- This pattern of binding multiple names to multiple values in a fixed-length sequence is called sequence unpacking; it is the same pattern that we see in assignment statements that bind multiple names to multiple values.
- [<map expression> for <name> in <sequence expression> if <filter expression>]
To evaluate a list comprehension, Python evaluates the <sequence expression>, which must return an iterable value. Then, for each element in order, the element value is bound to <name>, the filter expression is evaluated, and if it yields a true value, the map expression is evaluated. The values of the map expression are collected into a list.
- Slicing. Sequences contain smaller sequences within them. A slice of a sequence is any contiguous span of the original sequence, designated by a pair of integers. As with the range constructor, the first integer indicates the starting index of the slice and the second indicates one beyond the ending index.
- Primitive values such as numbers, strings, boolean values, and None appear within an element box. Composite values, such as function values and other lists, are indicated by an arrow.

## idea
- 必要的 基础的 抽象的 理论的 不太实际  少用的 频繁的 重要的  复杂的 
- 也不是说每一知识点都必须马上就要理解。
- 把学习时间当做是一种投资。复利的模式。。
- dive into python这么书里面 一些语法的用法。会说的更加的详细。。需要阅读。
- box-and-pointer pointer 指针 关系 指向 可以理解为等价的（但是不同同一个东西）
是box里面指向的哪个东西。。
- node tree leaf branch sub-tree 
- 有时候 一图胜千言 就是 ppt里面有很多概括 和图片的秒数。比文字秒数要清楚。。

## todo

## new words
- thereby :(formal) used to introduce the result of the action or situation mentioned
- in terms of:依据，按照; 在…方面;
- essence :he most important quality or feature of sth, that makes it what it is 本质；实质；精髓
- investigate :to carefully examine the facts of a situation, an event, a crime, etc. to find out the truth about it or how it happened 调查，侦查（某事）
- negated :to stop sth from having any effect 取消；使无效
- adjacent :(of an area, a building, a room, etc. 地区、建筑、房间等) next to or near sth 与…毗连的；邻近的
- approximation :
an estimate of a number or an amount that is almost correct, but not exact 近似值；粗略估算


- fractional :(formal) very small; not important 很小的；很少的；微不足道的
- finite :having a definite limit or fixed size 有限的；有限制的
- precision:the quality of being exact, accurate and careful 精确；准确；细致
	1. 
- truncated:to make sth shorter, especially by cutting off the top or end 截短，缩短，删节（尤指掐头或去尾）
	+ My article was published in truncated form.
- proficient: ~ (in/at doing sth) able to do sth well because of training and practice  
- pragmatic:solving problems in a practical and sensible way rather than by having fixed ideas or theories 实用的

- numerator 
- denominator
- glue 
- concrete 
- literal
- intuition 
- remedy 
- flaw 
- violation 
- constitute 
- barrier 
- sufficient 
- exhibiting 

- Sequences
- arbitrary 
- replicate 
- desired 
- pipeline 
- Aggregation
- perimeter 
- rectangle 
- indices
- omitted 
- ubiquitous 
- justified
- substantial ：large in amount, value or importance 大量的；价值巨大的；重大的
- commitment ：the willingness to work hard and give your energy and time to a job or an activity （对工作或某活动）献身，奉献，投入
- alphabet
- punctuation 
- diverges 
- Coercion
- descriptive 
- closure property of a data type.
- hierarchical ：arranged in a hierarchy 按等级划分的；等级制度的
- regularity ： the fact that the same thing happens again and again, and usually with the same length of time between each time it happens 规律性；经常性