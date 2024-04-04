n = int(input())
arr = []
cnt = 0
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in arr:
    if sum(i)/4 >= 60:
        print('pass')
        cnt+=1
    else:
        print('fail')
print(cnt)