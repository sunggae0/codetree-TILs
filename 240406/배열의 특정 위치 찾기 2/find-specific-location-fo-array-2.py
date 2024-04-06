arr = list(map(int,input().split()))

s1, s2 = 0, 0

for i in range(0,10,2):
    s1 += arr[i]
    s2 += arr[i+1]

result = s1 - s2
print(abs(result))