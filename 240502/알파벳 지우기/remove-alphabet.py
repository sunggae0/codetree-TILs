result = 0
for i in range(2):
    temp = ''
    for j in input():
        if 48<=ord(j)<=57:
            temp += j
    result += int(temp)

print(result)