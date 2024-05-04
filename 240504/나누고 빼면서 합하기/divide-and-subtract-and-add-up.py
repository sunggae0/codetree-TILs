n,m = map(int,input().split())
a = list(map(int,input().split()))

def func():
    global m
    if m%2 == 0:
        m=m//2
    else:
        m-=1

result = 0
while m >= 1:
    result += a[m-1]
    func()

print(result)