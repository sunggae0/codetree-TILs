def minn(arr):
    for i in arr:
        if i!=0:
            result = i
    for i in range(len(arr)):
        if arr[i] < result and arr[i] != 0:
            result = arr[i]
    return result

def find_min(arr):
    for i in range(n):
        if arr[i] == minn(arr):
            return i

n = int(input())
arr = list(map(int,input().split()))
indx = [0 for _ in range(n)]

for i in range(n):
    a = find_min(arr)
    indx[a] = i+1
    arr[a] = 0

print(*indx,sep = ' ')