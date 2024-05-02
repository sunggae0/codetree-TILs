n = int(input())
arr = list(map(int,input().split()))

min_num = 0
for i in range(n-1):
    for j in range(i+1,n):
        temp = abs(arr[i]-arr[j])
        if (i==0 and j==1) or min_num > temp:
            min_num = temp
print(min_num)