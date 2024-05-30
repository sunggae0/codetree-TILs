h1,m1,h2,m2 = map(int,input().split())

cnt = 0
while True:
    if h1 == h2 and m1 == m2:
        break
    else:
        m1 += 1
        if m1 == 60:
            h1+=1
            m1=0
        cnt += 1

print(cnt)