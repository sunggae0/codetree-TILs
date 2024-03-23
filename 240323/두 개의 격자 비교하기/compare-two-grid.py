x,y=map(int,input().split())
l1, l2, result = [], [], [[0 for _ in range(x)] for _ in range(y)]
for i in range(y):
    l1.append(list(map(int,input().split())))
for i in range(y):
    l2.append(list(map(int,input().split())))
for i in range(y):
    for j in range(x):
        if l1[i][j] != l2[i][j]:
            result[i][j] = 1
for i in result:
    for j in i:
        print(j, end = " ")
    print()