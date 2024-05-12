def f(depth):
    if depth == 1:
        return 1
    if depth == 2:
        return 2
    return f(depth//3) + f(depth - 1)

n = int(input())
print(f(n))