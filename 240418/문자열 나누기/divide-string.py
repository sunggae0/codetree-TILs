n = int(input())
t = input().split()
tt = ""
for i in t:
    tt += i
for i in range(len(tt)):
    print(tt[i],end="")
    if (i+1) % 5 == 0:
        print()