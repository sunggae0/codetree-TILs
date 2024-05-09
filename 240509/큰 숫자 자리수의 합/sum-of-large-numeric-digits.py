def f(t):
    if t=="":
        return 0
    return int(t[-1]) + f(t[:len(t)-1])

a,b,c=map(int,input().split())
print(f(str(a*b*c)))