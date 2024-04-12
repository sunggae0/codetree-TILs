arr = list(map(int,input().split()))

arr_cnt = [0] * 7

for i in arr:
    arr_cnt[i] += 1
for i in range(1,7):
    print("%d - %d"%(i,arr_cnt[i]))