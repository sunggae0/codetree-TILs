def result(a,o,c):
    if o == '+':
        return a+c
    elif o == '-':
        return a-c
    elif o == '*':
        return a*c
    elif o == '/':
        return int(a/c)
    else:
        return 'False'

a,o,c = input().split()

r = result(int(a),o,int(c))
print(int(a),o,int(c),'=',r) if r!='False' else print('False')