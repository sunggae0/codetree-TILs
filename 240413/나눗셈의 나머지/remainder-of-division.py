arr_cnt = [0]*4
a,b = map(int,input().split())

while a > 1:
    arr_cnt[a%b] += 1
    a = a//b

result = 0
for i in range(4):
    result += arr_cnt[i] ** 2
print(result)