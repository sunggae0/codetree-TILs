arr = list(map(int,input().split()))

tc = 0
h = 0

for i in arr:
    if i == 0:
        break
    if i%2 == 0:
        tc +=1
        h += i

print(tc,h)