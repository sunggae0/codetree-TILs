t = input()
result=''
for i in t:
    if i==t[1]:
        result += t[0]
    else:
        result += i
print(result)