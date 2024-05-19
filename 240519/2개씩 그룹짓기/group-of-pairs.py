def minimize_max_sum(N, nums):
    nums.sort()
    max_sum = 0
    
    for i in range(N):
        group_sum = nums[i] + nums[2 * N - 1 - i]
        if group_sum > max_sum:
            max_sum = group_sum
            
    return max_sum

# 입력
N = int(input())
nums = list(map(int, input().split()))

# 결과 출력
print(minimize_max_sum(N, nums))