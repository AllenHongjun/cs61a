# Higher-Order Functions record

## todolist
1. week 2 lab lec project..
2. 就算代码没有写完。。也要知道要做什么内容。。

## 感悟
1. To express certain general patterns as named concepts, we will need to construct functions that can accept other functions as arguments or return functions as values. Functions that manipulate functions are called higher-order functions. 类比于C#当中的委托。。
2. 黄金分割比例。这个计算的公式是怎么的出来的？？
3. 有的新的知识点。。第一遍看不懂也是正常。。疑惑先留着。调试调试代码。理解可能会深刻一些。

## 疑问
1.  Example: Newton's Method 公式计算的原理 不知道需要哪些数学知识
2. uncurry2 这个方法感觉有点绕。。
``` python
ef uncurry2(g):
        """Return a two-argument version of the given curried function."""
        def f(x, y):
            return g(x)(y)
        return f

```
3. lamdab表达式 : equel returns
4. @trace 

## 1.6 new word
1. suffice 
- arduous 
- manipulate:~ (sb into sth/into doing sth) (disapproving) to control or influence sb/sth, often in a dishonest way so that they do not realize it 
- mechanisms
- presence 
- apply:[动词 + 名词短语] ~ sth (to sth) to use sth or make sth work in a particular situation 使用；应用
- golden ratio:[计]黄金比例;
- intricate
- motion 
- virtue 
- incompatible 
- Consistent 
- Lexical scope.
- signify 
- conciselys
- Currying
- iterative 
- intermediate 
- intrinsic 
- notoriously 
- explicit 
- mechanism
- decorator
