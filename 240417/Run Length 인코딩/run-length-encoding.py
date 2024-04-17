t = input()
prev = t[0]
cnt = 0
result = ""
for i in t:
    if i == prev:
        cnt += 1
    else:
        result += prev + str(cnt)
        cnt = 1
    prev = i
result += prev + str(cnt)
print(len(result))
print(result)