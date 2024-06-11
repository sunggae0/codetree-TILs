result = 0
arr = [[0 for _ in range(2001)] for _ in range(2001)]

for i in range(2):
    x1,y1,x2,y2 = map(int,input().split())
    
    offset = -1000

    for j in range(min(y1,y2)-offset,max(y1,y2)-offset):
        for k in range(min(x1,x2)-offset,max(x1,x2)-offset):
            arr[j][k] = 1

x1,y1,x2,y2 = map(int,input().split())
    
offset = -1000

for j in range(min(y1,y2)-offset,max(y1,y2)-offset):
    for k in range(min(x1,x2)-offset,max(x1,x2)-offset):
        arr[j][k] = 2

for i in arr:
    for j in i:
        if j == 1:
            result +=1

print(result)