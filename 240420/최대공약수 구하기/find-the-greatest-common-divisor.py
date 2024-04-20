n,m = map(int,input().split())

def t(n,m):
    result = 0
    for i in range(1,max(n,m)+1):
        if n%i==0 and m%i==0 and i>result:
            result = i
    return result
 
print(t(n,m))