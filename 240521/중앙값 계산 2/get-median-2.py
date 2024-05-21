n = int(input())
arr = list(map(int,input().split()))

for i in range(1,n+1):
    if i%2!=0:
        temp = arr[:i]
        temp.sort()
        print(temp[len(temp)//2], end = ' ')