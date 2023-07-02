nums = [1, 4, 2, 10, 2, 3, 1, 0, 20]

k = 3

def max_subarray(nums: list, k: int):
    if k > len(nums):
        return None
    
    window_sum = sum(nums[:k])
    max_window_sum = window_sum

    for i in range(len(nums)-k):
        window_sum = window_sum - nums[i] + nums[i+k]
        max_window_sum = max(max_window_sum, window_sum)


    return max_window_sum


print(max_subarray(nums, k))
