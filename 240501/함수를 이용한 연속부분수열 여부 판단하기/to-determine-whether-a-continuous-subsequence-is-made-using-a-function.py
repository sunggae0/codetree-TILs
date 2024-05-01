def result(a,b):
    temp = False
    for i in range(len(a)-len(b)+1):
        if a[i:i+len(b)] == b:
            temp = True 
    return temp

n1,n2 = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

print('Yes') if result(a,b) else print('No')