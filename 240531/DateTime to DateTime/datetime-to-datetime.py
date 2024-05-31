a2,b2,c2 = map(int,input().split())
a1,b1,c1 = 11,11,11
cnt = 0
while True:
    if a1==a2 and b1==b2 and c1==c2:
        break
    c1 += 1
    cnt += 1
    if c1==60:
        b1+=1
        c1= 0
    if b1 == 24:
        a1+= 1
        b1=0
print(cnt)