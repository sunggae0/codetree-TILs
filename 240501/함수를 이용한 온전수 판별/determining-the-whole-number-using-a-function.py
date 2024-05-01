def result(n):
    return n%2!=0 and n%10!=5 and not(n%3==0 and n%9!=0)

a,b = map(int,input().split())

cnt = 0
for i in range(a,b+1):
    if result(i):
        cnt += 1
print(cnt)