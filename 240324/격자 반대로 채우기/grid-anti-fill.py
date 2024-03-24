n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
cnt = 1
arr_cnt = 0

for i in range(n-1,-1,-1):
    if arr_cnt % 2 == 0:
        for j in range(n-1, -1, -1):
            arr[j][i] = cnt
            cnt += 1
    else:
        for j in range(n):
            arr[j][i] = cnt
            cnt += 1
    arr_cnt += 1

for i in arr:
    for j in i:
        print(j, end = " ")
    print()