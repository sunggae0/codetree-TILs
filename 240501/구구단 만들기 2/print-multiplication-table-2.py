a,b = map(int,input().split())

for i in (2,4,6,8):
    for j in range(b,a-1,-1):
        print('%d * %d = %d'%(j,i,j*i),end=' ')
        if a<j<=b:
            print('/',end=' ')
    print()