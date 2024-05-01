n = int(input())

arr = []
for i in range(1,n+1):
    arr.append(n-(i-1))
    arr.append(i)

for i in arr:
    print('* '*i)