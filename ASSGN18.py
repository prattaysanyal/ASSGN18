# question 1
print('F = (b+c)(a-1)')

#question 2
x1 = -0.06
x2 = -2.5
x3 = 1.4

w1 = 2.7
w2 = -8.6
w3 = 0.002

X = (w1*x1) + (w2*x2) +(w3*x3)
print(X)

import math
In [4]:
fx = 1 / (1 + math.exp(-X))
print(fx)

bias = -1.1
newX = X + bias
print(newX)
