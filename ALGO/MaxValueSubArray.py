def maxSubArray(nums):
    # e = nums
    # temp = 0
    # result = 0
    # p = len(e)
    # for i in range(0, p):
    #     temp = 0
    #     for j in range(0, p):
    #         temp += e[j]
    #         result += temp
    # return result
    if len(nums) == 1:
        return nums[0]

    sum_r = [0 for i in range(len(nums))]
    sum_r[0] = nums[0]

    for i in range(1,len(nums)):
        if sum_r[i-1] < 0:
            sum_r[i] = nums[i]
        else:
            sum_r[i] = sum_r[i-1] + nums[i]

    return max(sum_r)



l = [4,-1,3,5,2]

print(maxSubArray(l))