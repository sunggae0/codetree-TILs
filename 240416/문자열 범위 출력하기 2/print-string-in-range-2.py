t = input()
n = int(input())

if n < len(t):
    for i in range(len(t)-1,len(t)-1-n,-1):
        print(t[i],end='')
else:
    for i in range(len(t)-1,-1,-1):
        print(t[i],end='')