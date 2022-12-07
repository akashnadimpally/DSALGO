def TwoSum(nums, target):
    if len(nums) == 1:
        return [0]

    sum_r = nums[0]
    p = []

    for i in range(1,len(nums)):
        t = sum_r + nums[i]
        if t == target:
            p.append(nums.index(sum_r))
            p.append(i)
            break
        else:
            sum_r = nums[i-1]

    return p



nums = [3,2,3]
target = 6
print(TwoSum(nums, target))