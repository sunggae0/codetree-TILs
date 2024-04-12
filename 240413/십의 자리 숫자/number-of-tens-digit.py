arr = list(map(int,input().split()))
arr_cnt = [0]*10

for i in range(len(arr)):
    if arr[i] == 0:
        cnt = i
        break

for i in range(cnt+1):
    arr_cnt[arr[i]//10] += 1

for i in range(1,10):
    print("%d - %d"%(i,arr_cnt[i]))