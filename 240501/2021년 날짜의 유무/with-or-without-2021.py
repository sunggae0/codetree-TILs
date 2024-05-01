def result(m,d):
    temp = True
    if m == 2:
        if d >28:
            temp = False
    elif 0<m<13:
        if m%2==0:
            if d>30:
                temp = False
        else:
            if d>31:
                temp = False
    else:
        temp = False
    return temp

m,d=map(int,input().split())

print('Yes') if result(m,d) else print('No')