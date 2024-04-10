arr = []
cnt = 0

for i in range(5):
    arr.append(int(input()))
for i in arr:
    cnt += 1 if i%2 == 0 else 0

print(cnt)