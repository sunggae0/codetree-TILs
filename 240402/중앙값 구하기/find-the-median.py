a = list(map(int,input().split()))

mid = 0

if a[1]<a[0]<a[2] or a[2]<a[0]<a[1]:
    print(a[0])
elif a[0]<a[1]<a[2] or a[2]<a[1]<a[0]:
    print(a[1])
else:
    print(a[2])