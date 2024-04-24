def oneinnum(n):
    t = str(n)
    return '3' in t or '6' in t or '9' in t

def check(n):
    return n%3==0 or oneinnum(n)


a,b = map(int,input().split())
cnt = 0
for i in range(a,b+1):
    if check(i):
        cnt += 1

print(cnt)