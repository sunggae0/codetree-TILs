num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m1,d1,m2,d2 = map(int,input().split())
cnt = 0

while True:
    if m1 == m2 and d1 == d2:
        break
    else:
        d1 += 1
        if d1 > num_of_days[m1]:
            m1 += 1
            d1 = 1
        cnt += 1
print(cnt+1)