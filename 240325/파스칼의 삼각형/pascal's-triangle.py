n = int(input())
arr = []
cnt = 1

for i in range(1,n+1):
    arr.append([1 for _ in range(i)])

for i in range(1,n):
    cnt = 1
    while cnt < len(arr[i-1]):
        arr[i][cnt] = arr[i-1][cnt] + arr[i-1][cnt-1]
        cnt += 1

for i in arr:
    for j in i:
        print(j, end = " ")
    print()