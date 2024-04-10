a,b = map(int,input().split())
mult = 1
for i in range(1,b+1):
    if i%a == 0:
        mult *= i

print(mult)