k = int(input())
arr=[0 for _ in range(1,101)]

for i in range(k):
    a,b=map(int,input().split())
    for j in range(a,b+1):
        arr[j]+=1

print(max(arr))