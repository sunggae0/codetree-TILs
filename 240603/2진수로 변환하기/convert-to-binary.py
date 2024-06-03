def demical2binary(n):
    arr=[]
    while True:
        if n<2:
            arr.append(n)
            break
        arr.append(n%2)
        n=n//2
    return arr[::-1]

n = int(input())

for i in demical2binary(n):
    print(i,end='')