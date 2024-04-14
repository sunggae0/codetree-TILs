arr = []
for i in range(10):
    arr.append(input())
t = input()
cnt = 0
for i in arr:
    if i[-1] == t:
        print(i)
        cnt += 1
print('None') if not(cnt) else 0