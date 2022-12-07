# def searchInsert(nums: list[int], target: int) -> int:


def helper(nums, low, high, target):

    if (target in nums):
        if (high >= low):
            mid = (low + high) // 2
            if (nums[mid] > target):
                high = mid - 1
                return helper(nums,low,high,target)
            elif (nums[mid] < target):
                low = mid + 1
                return helper(nums, low, high, target)
            else:
                return mid
    else:
        nums.append(target)
        r = sorted(nums)
        low_r = 0
        high_r = len(r) - 1
        return helper(r, low_r, high_r, target)

    #
    #
    # while (low <= high):
    #     mid = (low + high) // 2
    #     if (nums[mid] > target):
    #         high = mid - 1
    #     elif (nums[mid] < target):
    #         low = mid + 1
    #     elif (nums[mid] == target):
    #         return mid
    #     else:
    #         nums.append(target)
    #         r = sorted(nums)
    #         return nums.index(target)
    #

l = [1,3,5,6]
target = 7

low = 0
high = len(l) - 1

print(helper(l, low, high, target))