def days(m2,d2):
    m1,d1,cnt = 1,1,0
    while m1!=m2 or d1!=d2:
        d1 += 1
        cnt+=1
        if d1 > m[m1]:
            m1+=1
            d1=1
    return cnt

m1,d1,m2,d2 = map(int,input().split())
a = input()
m = [31,29,31,30,31,30,31,31,30,31,30,31]
d=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']

selected_day = d.index(a) + 1
cnt=0
for i in range(days(m1,d1),days(m2,d2)+1):
    if (i)%7==selected_day-1:
        cnt+=1
print(cnt)