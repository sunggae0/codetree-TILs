def f(depth):
    if depth == 1:
        return 2
    if depth == 2:
        return 4
    return f(depth-1) * f(depth-2) % 100

n = int(input())
print(f(n))