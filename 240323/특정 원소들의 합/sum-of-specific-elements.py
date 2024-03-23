arr = []
for i in range(4):
    arr.append(list(map(int,input().split())))
result = 0
for i in range(1,5):
    for j in range(i):
        result += arr[i-1][j]
print(result)