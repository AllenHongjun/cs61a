# Numeric expressions
2020
2000 + 20
-1 + 2 + 3 + 4 * ((5 // 6) + 7 * 8 * 9)

# Call expressions
max(3, 4.5)
pow(100, 2)
pow(2, 100)
max(1, -2, 3, -4)

# Importing and arithmetic with call expressions
from operator import add, mul
add(1, 2)
mul(4, 6)
mul(add(4, mul(4, 6)), add(3, 5))
add(4, mul(9, mul(add(4, mul(4, 6)), add(3, 5))))

# Objects
# Note: Download from http://composingprograms.com/shakespeare.txt
shakes = open('shakespeare.txt')
text = shakes.read().split()
len(text)
text[:25]
text.count('the')
text.count('thou')
text.count('you')
text.count('forsooth')
text.count(',')

# Sets
words = set(text)
len(words)
max(words)
max(words, key=len)

# Reversals
'draw'[::-1]
{w for w in words if w == w[::-1] and len(w)>4}
{w for w in words if w[::-1] in words and len(w) == 4}
{w for w in words if w[::-1] in words and len(w) > 6}
