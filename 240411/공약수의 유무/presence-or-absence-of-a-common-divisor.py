a,b = map(int,input().split())
result = False
for i in range(a,b+1):
    if (1920%i == 0 and 2880%i == 0):
        result = True
        break
if result == True:
    print(1) 
else:
    print(0)