a,b = map(int,input().split())
absum = 0

for i in range(a,b+1):
    absum += i if i%6==0 and i%8!=0 else 0
        
print(absum)