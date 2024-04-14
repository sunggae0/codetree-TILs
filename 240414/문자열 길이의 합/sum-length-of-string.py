n = int(input())
cnt = 0
acnt = 0
for i in range(n):
    t = input()
    cnt += len(t)
    acnt += 1 if t[0] == 'a' else 0
print(cnt,acnt)