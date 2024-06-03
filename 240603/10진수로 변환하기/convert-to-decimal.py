def binary2demical(arr):
    n = 0
    for i in arr:
        n = n*2+int(i)
    return n

binary = list(input())

print(binary2demical(binary))