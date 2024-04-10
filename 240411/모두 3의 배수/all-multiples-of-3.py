result = True
for i in range(5):
    if int(input())%3!=0:
        result = False
        break
print(1) if result else print(0)