p1 = input().split()
p2 = input().split()
result = 0

if int(p1[0]) >= 19 and p1[1] == 'M':
    result = 1
elif int(p2[0]) >= 19 and p2[1] == 'M':
    result = 1
print(result)