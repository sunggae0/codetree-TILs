n = int(input())

for i in range(n):
    result = 0
    a,b=map(int,input().split())
    for i in range(a,b+1):
        result += i if i%2==0 else 0
    print(result)