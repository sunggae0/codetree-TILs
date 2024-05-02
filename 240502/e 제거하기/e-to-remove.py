t = input()
temp = False
for i in t:
    if i!='e':
        print(i,end='')
    elif temp == False:
        temp = True
    else:
        print(i,end='')