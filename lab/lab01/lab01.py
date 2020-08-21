

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    m = 1
    while( k > 0):
        m =  m * n  
        n = n -1
        k = k -1
        # """print("m:----",m,"n:-----",n,"k:-----",k)"""
    print(m)
    

## sum the digits 
def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    # 边界值的判断
    sum = 0
    a = 0
    b = y
    while(b>0):
        
        a = b % 10
        sum += a
        b = b // 10
        #print("a:",a,"y:",y,"sum:",sum,"b:",b)
    #print(sum)
    return sum
    




## count there are how many eight in a squence of number
## 判断这一串数字是否有两个临近的8
## 理解题意。。写代码的工具 容易阅读。。以后还是要阅读的。
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    m = 0
    isTrue = False

    while( n > 0):
        m = n % 10
        if( m == 8):
            if((n // 10) % 10 == 8):
                isTrue = True
        n = n // 10
    return isTrue


    # count_of_eight = 0
    # divide_of_n = 0
    # has_two_eight = False

    # while( n > 0):
    #     divide_of_n = n % 10
    #     n = n // 10
    #     if(divide_of_n == 8):
    #         count_of_eight = count_of_eight + 1
    #     ##print("divide_of_n:",divide_of_n,"n:",n,"count_of_eight",count_of_eight)
    
    # if(count_of_eight == 2):
    #     has_two_eight = True
    # else:
    #     has_two_eight = False
    
    # return has_two_eight

    



