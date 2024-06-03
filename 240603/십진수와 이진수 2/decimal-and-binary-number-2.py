def dem2bin(n):
    arr=[]
    while True:
        if n<2:
            arr.append(n)
            break
        arr.append(n%2)
        n=n//2
    return arr[::-1]

def bin2dem(n):
    num=0
    for i in str(n):
        num=num*2+int(i)
    return num

n = int(input())
n = bin2dem(n)
n*=17
n = dem2bin(n)

for i in n:
    print(i,end='')