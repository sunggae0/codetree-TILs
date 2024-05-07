def result(cnt):
    if cnt==0:
        return
    print('*'*cnt)
    result(cnt-1)
    print('*'*cnt)

n = int(input())
result(n)