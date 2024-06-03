def demical2anynum(n,b):
    arr=[]
    while True:
        if n<b:
            arr.append(n)
            break
        arr.append(n%b)
        n=n//b
    return arr[::-1]

n,b=map(int,input().split())

for i in demical2anynum(n,b):
    print(i,end='')