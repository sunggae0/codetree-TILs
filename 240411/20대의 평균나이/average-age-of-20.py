arr = []
while True:
    n = int(input())
    if 20<=n<=29:
        arr.append(n)
    else:
        break

print("%.2f"%(sum(arr)/len(arr)))