# def quick_sort(nums):
#     n = len(nums)
#     if n<=1:
#         return nums
#     else:
#         pivot = nums.pop()
#
#     l = []
#     r = []
#     for i in nums:
#         if (i<pivot):
#             l.append(i)
#         else:
#             r.append(i)
#     return quick_sort(l)+[pivot]+quick_sort(r)
#
# def binary_search(nums,target):
#     n = len(nums)
#     low = 0
#     high = n-1
#     while(low<=high):
#         mid = (low+high)//2
#         if (nums[mid]<target):
#             low = mid + 1
#         elif (nums[mid]>target):
#             high = mid - 1
#         else:
#             return mid
#
#
# nums = [1,2]
# h = quick_sort(nums)
# length = len(nums)
#
# if length <= 2:
#     y = h[-1]
#     # print(1)
#     print(y)
#     if y in nums:
#         print(nums.index(y))
#     else:
#         print(0)
#
# else:
#     target = h[-1]
#     # print(binary_search(nums, target))
#     index = binary_search(nums, target)
#     if index != -1:
#         print(index)
#     else:
#         print(0)

def peak_element(nums):
    n = len(nums)
    if n<=1:
        return 0
    else:
        l = 0
        h = n-1
        while (l<h):
            mid = (l+h)//2
            if (nums[mid] < nums[mid+1]):
                l = mid +1
            else:
                h = mid
        return l

nums = [1,2]

print(peak_element(nums))