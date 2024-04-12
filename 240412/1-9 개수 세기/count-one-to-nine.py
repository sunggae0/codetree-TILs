n = int(input())
arr_cnt = [0] * 10

arr = list(map(int,input().split()))
for i in arr:
    arr_cnt[i] += 1
for i in range(1,10):
    print(arr_cnt[i])