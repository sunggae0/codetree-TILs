def is_prime(n):
    result = True
    for i in range(2,n):
        if n%i == 0:
            result = False
            break
    return result

a,b = map(int,input().split())

result = 0
for i in range(a,b+1):
    if is_prime(i) == True and i != 1:
        result += i

print(result)