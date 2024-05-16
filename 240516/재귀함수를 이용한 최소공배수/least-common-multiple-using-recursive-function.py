def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_of_list(nums, n):
    if n == 1:
        return nums[0]
    else:
        return lcm(nums[n-1], lcm_of_list(nums, n-1))

# 입력 처리
n = int(input().strip())
numbers = list(map(int, input().strip().split()))

# 최소공배수 계산
result = lcm_of_list(numbers, n)
print(result)