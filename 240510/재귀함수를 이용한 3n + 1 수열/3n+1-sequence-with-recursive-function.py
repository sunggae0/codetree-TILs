def f(x,depth):
    if x==1:
        return depth
    if x%2==0:
        return f(x//2,depth+1)
    else:
        return f(x*3+1,depth+1)

print(f(int(input()),0))