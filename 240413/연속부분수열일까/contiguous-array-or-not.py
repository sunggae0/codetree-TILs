n1,n2 = map(int,input().split())

a = list(map(int,input().split()))
b=  list(map(int,input().split()))

p = 0
while p<= n1-n2:
    result = True
    for i in range(p,p+n2):
        if a[i] != b[i-p]:
            result = False
    p += 1
    if result == True:
        break

if result == True:
    print("Yes")
else:
    print("No")