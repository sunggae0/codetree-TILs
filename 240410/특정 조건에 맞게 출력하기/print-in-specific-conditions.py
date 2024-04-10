arr = list(map(int,input().split()))

for i in arr:
    if i == 0:
        pass
    elif i%2 == 0:
        print(int(i/2),end = " ")
    else:
        print(i+3,end=" ")