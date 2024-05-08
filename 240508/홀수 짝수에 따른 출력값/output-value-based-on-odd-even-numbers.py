def func1(n):
    if n == 2:
        return 2
    if n%2 != 0:
        return func1(n-1)
    else:
        return n + func1(n-1)

def func2(n):
    if n == 1:
        return 1
    if n%2 == 0:
        return func2(n-1)
    else:
        return n + func2(n-1)

def judge(n):
    if n%2==0:
        return func1(n)
    else:
        return func2(n)

n = int(input())
print(judge(n))