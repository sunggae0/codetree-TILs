cnt = 0
last = 0
arr = []

n = int(input())
for i in range(n):
    temp = int(input())
    if i==0 or last != temp:
        arr.append(0)
        cnt +=1
    last = temp
    arr[cnt-1]+=1

print(max(arr))