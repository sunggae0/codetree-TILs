n, m = map(int,input().split())
arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    pos = list(map(int,input().split()))
    arr[pos[0]-1][pos[1]-1] = pos[0] * pos[1]

for i in arr:
    for j in i:
        print(j, end = " ")
    print()