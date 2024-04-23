def result(n):
    h = 0
    for i in range(1,n+1):
        h += i
    return int(h/10)

n = int(input())
print(result(n))