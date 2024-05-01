def func_abs(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])

n = int(input())

arr = list(map(int,input().split()))
func_abs(arr)
for i in arr:
    print(i,end=' ')