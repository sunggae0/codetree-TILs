def days(m2,d2):
    m1,d1=1,1
    cnt = 0
    while m1!=m2 and d2!=d1:
        d1+=1
        if d1 == m[m2]:
            m1+=1
            d1=1
        cnt+=1
    return cnt


m1,d1,m2,d2 = map(int,input().split())
m = [0,31,28,31,30,31,30,31,31,30,31,30,31]
d=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']

d_num=1

if days(m1,d1) > days(m2,d2):
    while True:
        if m1==m2 and d1==d2:
            break
        d1-=1
        d_num-=1
        if d1==m[m1]:
            m1-=1
            d1=1
else:
    while True:
        if m1==m2 and d1==d2:
            break
        d1+=1
        d_num+=1
        if d1==m[m1]:
            m1+=1
            d1=1

print(d[d_num%7])