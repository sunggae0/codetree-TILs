n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
for i in arr:
    if i%2 != 0:
        print(i)