a1,a2 = map(int,input().split())
a = [a1,a2]

for i in range(2,10):
    a.append(a[i-1] + 2*a[i-2])

for i in a:
    print(i, end=" ")