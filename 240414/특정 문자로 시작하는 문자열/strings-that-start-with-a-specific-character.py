n = int(input())
arr = []
for i in range(n):
    arr.append(input())
t = input()

cnt = 0
t_sum = 0
for i in arr:
    if i[0] == t:
        cnt += 1
        t_sum += len(i)
print("%d %.2f"%(cnt,t_sum/cnt))