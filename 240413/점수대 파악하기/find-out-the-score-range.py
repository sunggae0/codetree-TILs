arr = list(map(int,input().split()))
arr_cnt = [0]*11

for i in range(len(arr)):
    if arr[i] == 0:
        cnt = i
        break

for i in range(cnt):
    arr_cnt[arr[i]//10] += 1

for i in range(10,0,-1):
    print("%d0 - %d"%(i,arr_cnt[i]))