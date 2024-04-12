data = []
result = [0] * 4
for i in range(3):
    data.append(input().split())
for i in data:
    if i[0] == 'Y' and int(i[1])>=37:
        result[0] += 1
    elif i[0] == 'N' and int(i[1])>=37:
        result[1] += 1
    elif i[0] == 'Y' and int(i[1])<37:
        result[2] += 1
    else:
        result[3] += 1

for i in result:
    print(i,end=" ")
if result[0] >= 2:
    print("E")