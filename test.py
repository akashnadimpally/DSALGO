def twoSum(nums, target):
    sum_r = nums[0]
    r = []
    for i in range(1, len(nums)):
        print("sum_r: ", sum_r)
        sum_r = sum_r + nums[i]
        print("sum_r: ", sum_r)
        if (sum_r == target):
            r.append(i - 1)
            r.append(i)
            return r
        else:
            sum_r = nums[i]
            print("sum_r: ", sum_r)

        print("--------------------------------")


nums = [3,2,3]
target = 6

print(twoSum(nums,target))