arr = list(map(int,input().split()))
cnt=0
sm=0
for i in arr:
    if i == 0:
        break
    cnt+=1
for i in range(cnt-1,cnt-5,-1):
    sm+=arr[i]
print(sm)