n = int(input())

def sqr(n):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if cnt < 9:
                cnt+=1
            else:
                cnt = 1
            print(cnt, end=' ')
        print()
sqr(n)