a = list(map(int,input().split()))
asum = 0
cnt = 0
for i in a:
    if i >= 250:
        break
    asum += i
    cnt +=1

print("%d%.1f"%(asum, asum/cnt))