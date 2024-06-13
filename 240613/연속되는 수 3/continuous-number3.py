cnt=0
arr=[]
last = 0

n = int(input())
for i in range(n):
    temp = int(input())
    if i==0 or last * temp < 0:
        cnt+=1
        arr.append(0)
    last = temp
    arr[cnt-1] += 1

print(max(arr))