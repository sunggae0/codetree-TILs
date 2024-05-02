n = int(input())

cnt = 65
for i in range(n,0,-1):
    for j in range(n-i):
        print(' ',end=' ')
    for j in range(i):
        print(chr(cnt),end=' ')
        if cnt < 90:
            cnt+=1
        else:
            cnt = 65
    print()