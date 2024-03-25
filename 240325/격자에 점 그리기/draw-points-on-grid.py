n, m = map(int,input().split())
arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(1,m+1):
    pos = list(map(int,input().split()))
    arr[pos[0]-1][pos[1]-1] = i

for i in arr:
    for j in i:
        print(j, end = " ")
    print()