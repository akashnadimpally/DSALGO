# def quick_sort(nums):
#     n = len(nums)
#     if n<=1:
#         return nums
#     else:
#         pivot = nums.pop()
    
#     l = []
#     r = []
#     for i in nums:
#         if (i<pivot):
#             l.append(i)
#         else:
#             r.append(i)
#     return quick_sort(l)+[pivot]+quick_sort(r)

nums = [1,2,3,1]
# h = quick_sort(nums)

print(max(nums))