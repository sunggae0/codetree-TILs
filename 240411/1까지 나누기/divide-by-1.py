n = int(input())
cnt = 0

while n > 1:
    cnt += 1
    n = n//cnt
print(cnt)