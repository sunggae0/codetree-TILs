def find_min(arr):
    for i in range(n):
        if arr[i] == min(arr):
            return i

n = int(input())
arr = list(map(int,input().split()))
indx = [0 for _ in range(n)]

for i in range(n):
    a = find_min(arr)
    indx[a] = i+1
    arr[a] = 1000001

print(*indx,sep = ' ')