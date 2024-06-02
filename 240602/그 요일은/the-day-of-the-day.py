def days(m2,d2):
    m1,d1,cnt = 1,1,0
    while True:
        if m1==m2 and d1==d2:
            break
        d1 +=1
        cnt += 1
        if d1 > m[m1]:
            d1=1
            m1+=1
    return cnt

m = [0,31,29,31,30,31,30,31,31,30,31,30,31]
d = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

m1,d1,m2,d2 = map(int,input().split())
selected = d.index(input())

day1 = days(m1,d1)
day2 = days(m2,d2)
cnt=0
for i in range(day2-day1+1):
    if i%7 == selected:
        cnt+=1
print(cnt)