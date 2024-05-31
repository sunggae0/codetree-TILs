a2,b2,c2 = map(int,input().split())
a1,b1,c1 = 11,11,11
result = (c2-c1)+(b2-b1)*60+(a2-a1)*60*24
if result >= 0:
    print(result)
else:
    print(-1)