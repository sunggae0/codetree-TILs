n = int(input())
nums = 0
for i in range(n):
    nums += int(input())
result = str(nums)
result = result[1:] + result[0]
print(result)