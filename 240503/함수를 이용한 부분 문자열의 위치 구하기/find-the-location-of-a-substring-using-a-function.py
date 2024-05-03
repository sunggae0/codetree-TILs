t = input()
o = input()
tl = len(t)
ol = len(o)

def result(i):
    for j in range(ol):
        if t[i+j] != o[j]:
            return False
    return True

temp = False
for i in range(tl-ol+1):
    if result(i):
        print(i)
        temp = True
if not(temp):
    print(-1)