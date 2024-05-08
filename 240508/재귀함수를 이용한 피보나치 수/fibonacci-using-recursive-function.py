def result(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    return result(n-1) + result(n-2)

n = int(input())
print(result(n))