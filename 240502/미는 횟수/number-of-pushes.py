a=input()
b=input()

cnt=0
while a!=b:
    a = a[-1] + a[0:len(a)-1]
    cnt += 1
    if cnt > len(a):
        cnt = -1
        break

print(cnt)