arr = ["apple", "banana", "grape", "blueberry", "orange"]
t = input()
cnt = 0
for i in arr:
    if i[3] == t or i[2] == t:
        print(i)
        cnt += 1
print(cnt)