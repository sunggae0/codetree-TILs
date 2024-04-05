arr = list(map(int,input().split()))
s2=0
a3=0
for i in range(1,10,2):
    s2+=arr[i]

for i in range(2,10,3):
    a3+=arr[i]
a3/=3

print("%d %.1f"%(s2,a3))