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

print(int(a),o,int(c),'=',result(int(a),o,int(c)))