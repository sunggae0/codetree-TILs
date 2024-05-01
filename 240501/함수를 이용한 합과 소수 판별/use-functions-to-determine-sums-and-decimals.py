def prime(n):
    result = True
    for i in range(2,n):
        if n%i == 0:
            result = False
    return result

def hap(n):
    result = 0
    while n>0:
        result += n%10
        n=n//10
    return result

def result(n):
    return prime(n) and hap(n)%2==0

a,b = map(int,input().split())

cnt = 0
for i in range(a,b+1):
    cnt += 1 if result(i) else 0
print(cnt)