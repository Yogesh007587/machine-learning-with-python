import numpy as np1
a = np1.array([1,2,3,4])
print(type(a))
print(a.shape)
print(a[1])
b=np1.array([[1,2,3],[5,6,7]])
print(b.shape)
d=np1.array([4,5,656,5],dtype=float)
print(d)
print(3*a)
print(3 in b)
eye=np1.eye(4)
print(eye)
one=np1.ones((2,3))
print(one)
zero=np1.zeros((3,5))
print(zero)
a.fill(1)
print(a)
c=np1.full((3,3),7)
print(c)
print(np1.sum(c))
print(np1.mean(c))
print(np1.std(c))
