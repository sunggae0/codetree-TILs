n, m = map(int,input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
start_pos = [0,0]
current_pos = [0,0]
cnt = 1

while start_pos[0] <= m-1 and start_pos[1] <= n-1:
    current_pos[0], current_pos[1] = start_pos[0], start_pos[1]
    while current_pos[0] >= 0 and current_pos[1] <= n-1:
        arr[current_pos[1]][current_pos[0]] = cnt
        current_pos[0] -= 1
        current_pos[1] += 1
        cnt += 1
    if start_pos[0] < m-1:
        start_pos[0] += 1
    else:
        start_pos[0] = m-1
        start_pos[1] += 1

for i in arr:
    for j in i:
        print(j, end = " ")
    print()