n = int(input())

arr = [1,n]

cnt = 2
while arr[cnt-1] + arr[cnt-2] < 100:
    arr.append(arr[cnt-1] + arr[cnt-2])
    cnt += 1
arr.append(arr[cnt-1] + arr[cnt-2])

for i in arr:
    print(i, end = " ")