def result(n):
    if n<10:
        return n**2
    return result(n//10) + (n%10)**2
n=int(input())
print(result(n))