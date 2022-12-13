def binary_search(nums, target):
    low = 0
    high = len(nums)

    while (high >= low):
        mid = (low + high) // 2
        if (nums[mid] > target):
            high = mid - 1
        elif (nums[mid] < target):
            low = mid + 1
        else:
            return mid

    return -1


nums = [5,7,7,8,8,10]
target = 8

l = []

if len(nums) <= 1:
    if target in nums:
        return [0, 0]

for i in range(len(nums)):
    if nums[i] == target:
        l.append(i)

r = [-1, -1]
if l == []:
    return r
elif len(l) == 1:
    t = l[0]
    l.append(t)
    return l
elif len(l) > 2:
    ans = [l[0], l[-1]]
    return ans
else:
    return l

