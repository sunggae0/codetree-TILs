n,k,t = input().split()
n = int(n); k = int(k)

arr = []
for i in range(n):
    temp = input()
    if temp[:len(t)] == t:
        arr.append(temp)

arr.sort()
print(arr[k-1])