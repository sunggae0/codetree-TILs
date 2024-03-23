a,b=map(int,input().split())
cnt = 0
for i in range(a):
    for j in range(b):
        cnt +=1
        print(cnt,end = " ")
    print()