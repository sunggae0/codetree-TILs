n = int(input())

cnt = 0
loop = 1

while cnt < 2:
    print(n*loop, end=" ")
    if (n*loop) % 5 == 0:
        cnt +=1
    loop += 1