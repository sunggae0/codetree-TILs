arr = list(map(int,input().split()))

cnt = 0
for i in arr:
    if i == 0:
        break
    cnt +=1

for i in range(cnt):
    h += arr[i]
print("%d %.1f"%(h, h/cnt))