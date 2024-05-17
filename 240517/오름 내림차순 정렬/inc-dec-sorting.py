n = int(input())
arr = list(map(int,input().split()))

arr.sort()

for i in arr:
    print(i,end=' ')

print()
arr = arr[::-1]

for i in arr:
    print(i,end=' ')