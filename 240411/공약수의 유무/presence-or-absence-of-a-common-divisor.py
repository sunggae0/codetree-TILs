a,b = map(int,input().split())
result = False
for i in range(a,b+1):
    for j in range(2,i+1):
        if (1920%j == 0 and i%j == 0)  or (2880%j == 0 and i%j == 0):
            result = True
            break
    if result == True:
        break
if result == True:
    print(1) 
else:
    print(0)