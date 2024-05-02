t = input()
b = input()

cnt = 0
for i in range(len(t)-len(b)+1):
    if t[i:i+len(b)] == b:
        cnt += 1
print(cnt)