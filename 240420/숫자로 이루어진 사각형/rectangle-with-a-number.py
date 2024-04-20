n = int(input())

def sqr(n):
    for i in range(n):
        for j in range(n):
            print(j+4*i, end = ' ')
        print()

sqr(n)