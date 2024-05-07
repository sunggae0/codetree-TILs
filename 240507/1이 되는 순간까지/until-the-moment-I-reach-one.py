cnt = 0

def result(n):
    global cnt
    if n==1:
        return cnt
    if n%2==0:
        cnt+=1
        return result(n//2)
    else:
        cnt+=1
        return result(n//3)

n = int(input())
print(result(n))