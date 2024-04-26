def un(n):
    result = False
    if n%100==0:
        if n%400 != 0: 
            result = True
    else:
        if n%4==0:
            result = True
    return result

y = int(input())
print('true') if un(y) == True else print('false')