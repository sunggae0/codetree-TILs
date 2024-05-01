def judge(t):
    return t==t[-1:-(len(t))-1:-1]

a=input()
print('Yes') if judge(a) else print('No')