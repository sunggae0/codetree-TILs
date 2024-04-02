arr = list(map(int,input().split()))
cnt = 0
for i in arr:
    if i == 0:
        break
    cnt += 1

for i in range(cnt-1,-1,-1):
    if arr[i] != 0:
        print(arr[i], end = " ")