n1,n2 = map(int,input().split())

a = list(map(int,input().split()))
b=  list(map(int,input().split()))

p = 0
result = False
while p<= n1-n2 and result == False:
    result = True
    for i in range(p,p+n2):
        if a[i] != b[i-p]:
            result = False
            break
    p += 1

if result == True:
    print("Yes")
else:
    print("No")