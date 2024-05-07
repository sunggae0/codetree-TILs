def result(cnt):
    if cnt == 0:
        return
    print(cnt,end=' ')
    result(cnt-1)
    print(cnt,end=' ')

n = int(input())
result(n)