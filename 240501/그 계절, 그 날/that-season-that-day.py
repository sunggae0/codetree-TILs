def yun(y):
    if y%4==0:
        if y%100==0:
            if y%400==0:
                return True
            return False
        return True
    return False

def date_check(y,m):
    if m==2:
        if yun(y):
            return 29
        return 28
    else:
        if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
            return 31
        else:
            return 30

def judge_md(y,m,d):
    if d>date_check(y,m):
        return False
    else:
        return True

y,m,d = map(int,input().split())

if judge_md(y,m,d):
    if 2<m<6:
        print("Spring")
    elif 5<m<9:
        print("Summer")
    elif 8<m<12:
        print("Fall")
    else:
        print("Winter")

else:
    print(-1)