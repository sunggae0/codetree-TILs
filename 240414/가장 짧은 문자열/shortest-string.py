arr=[]
arr_cnt = []
for i in range(3):
    arr.append(input())
    arr_cnt.append(len(arr[i]))
print(max(arr_cnt)-min(arr_cnt))