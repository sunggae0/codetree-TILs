n = int(input())
arr = list(map(int,input().split()))
def f(cnt):
    result = True
    for i in arr:
        if cnt % i != 0:
            result = False
    if result:
        return cnt
    return f(cnt+min(arr))

print(f(max(arr)))