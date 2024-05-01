def result(a,b):
    temp = False
    for i in range(len(a)-len(b)):
        temp = True if a[i:i+len(b)] == b else 0
    return temp

n1,n2 = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

print('No') if result(a,b) else print('Yes')