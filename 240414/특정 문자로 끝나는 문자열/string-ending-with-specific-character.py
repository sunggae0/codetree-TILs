arr = []
for i in range(10):
    arr.append(input())
t = input()
for i in arr:
    if i[-1] == t:
        print(i)