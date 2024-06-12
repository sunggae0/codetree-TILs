n = int(input())
color = 0 #0red 1blue
offset = 100

arr = [[0 for _ in range(201)] for _ in range(201)]

for i in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    for j in range(y1+offset,y2+offset):
        for k in range(x1+offset,x2+offset):
            arr[j][k] = color%2
    color+=1

cnt = 0
for i in arr:
    for j in i:
        if j==1:
            cnt+=1

print(cnt)