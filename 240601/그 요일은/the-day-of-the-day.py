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
for i in range(day1,day2+1):
    if i%7 == selected:
        cnt+=1
print(cnt)
'''

def days(m2,d2):
    m1, d1, cnt = 1, 1, 0
    while True:
        if m1 == m2 and d1 == d2:
            break
        d1 += 1
        cnt += 1
        if d1 > m[m1]:
            d1 = 1
            m1 += 1
    return cnt

# 월별 일수, 윤년을 가정하며 2월은 29일
m = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 2월 5일까지의 일수 계산
print(days(2, 5))  # 예상 출력: 1월 31일 + 2월 4일 = 35일
'''