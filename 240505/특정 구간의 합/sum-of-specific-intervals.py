n,m = map(int,input().split())
a = list(map(int,input().split()))

def result(a1,a2):
    temp = 0
    for i in range(a1-1,a2):
        temp += a[i]
    return temp

for i in range(m):
    a1,a2 = map(int,input().split())
    print(result(a1,a2))