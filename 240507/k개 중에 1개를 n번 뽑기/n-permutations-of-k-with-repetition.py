k,n = map(int,input().split())
def printnum(arr):
    for i in arr:
        print(i,end=' ')
    print()

arr=[]
def gen(depth):
    global arr
    if depth == n+1:
        printnum(arr)
        return
    
    for i in range(1,k+1):
        arr.append(i)
        gen(depth+1)
        arr.pop()

gen(1)