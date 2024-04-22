n,m = map(int,input().split())

cnt = 0
s=min(n,m)
b=max(n,m)
while True:
    cnt += 1
    if (s*cnt) % b == 0:
        break

print(s*cnt)