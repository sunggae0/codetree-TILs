n = int(input())
arr = list(map(int,input().split()))
maxx = 0

def result(arr):
    global maxx
    if len(arr) == 0:
        return maxx
    if arr[-1] > maxx:
        maxx = arr[-1]
    return result(arr[:len(arr)-1])

print(result(arr))