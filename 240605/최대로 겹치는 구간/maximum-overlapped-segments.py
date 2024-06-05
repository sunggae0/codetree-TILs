k = int(input())
arr=[0 for _ in range(-100,101)]

for i in range(k):
    a,b=map(int,input().split())
    for j in range(a+100,b+100):
        arr[j]+=1

print(max(arr))