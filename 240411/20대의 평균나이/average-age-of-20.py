arr = []
while True:
    n = int(input())
    if n>=30:
        break
    else:
        arr.append(n)

print("%.2f"%(sum(arr)/len(arr)))