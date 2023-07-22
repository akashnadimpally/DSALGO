def quick_sort(nums):
    n = len(nums)
    if n<=1:
        return nums
    else:
        left = []
        right = []
        pivot = nums.pop()
        for i in nums:
            if (nums[i]<pivot):
                left.append(nums[i])
            else:
                right.append(nums[i])
        return quick_sort(left)+[pivot]+quick_sort(right)

# spells = [5,1,3]
# potions = [1,2,3,4,5]
# success = 7

spells = [3,1,2]
potions = [8,5,8]
success = 16

potions = quick_sort(potions)
ans = []
m = len(potions)
maxPotion = max(potions)



# k = []
# for i in spells:
#     t = [i*j for j in potions]
#     k.append(t)
#
# print(k)
# res = []
# for z in k:
#     c = 0
#     for q in z:
#         if q >= success:
#             c+=1
#     res.append(c)
# print(res)

# res = []
#
# for i in spells:
#     c = 0
#     for j in potions:
#         t = i*j
#         if t>=success:
#             c+=1
#     res.append(c)
#
# print(res)

