n = int(input())
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(i,'*',j,'=',i*j,end = ' ')
        print('/',end=' ') if 1<=j<n-i+1 else 0
    print()