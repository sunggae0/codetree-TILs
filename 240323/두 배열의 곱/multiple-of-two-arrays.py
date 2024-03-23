l1, l2 = [], []
for i in range(3):
    l1.append(list(map(int,input().split())))
none = input()
for i in range(3):
    l2.append(list(map(int,input().split())))
for i in range(3):
    for j in range(3):
        print(l1[i][j] * l2[i][j], end = " ")
    print()