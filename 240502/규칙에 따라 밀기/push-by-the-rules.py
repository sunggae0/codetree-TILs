a=input()
comm = 0
for i in input():
    if i=='L':
        comm += 1
    elif i=='R':
        comm -= 1


for i in range(len(a)):
    print(a[comm],end='')
    if comm < len(a)-1:
        comm += 1
    else:
        comm = 0