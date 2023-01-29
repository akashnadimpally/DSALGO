nums1 = [1,2]
nums2 = [3,4]

n = nums1 + nums2

def quick_sort(n):

    right = []
    left = []
    middle_n = []

    if len(n) <= 1:
        return n

    else:
        pivot = n[0]
        for i in n:
            if i < pivot:
                left.append(i)
            elif i == pivot:
                middle_n.append(i)
            else:
                right.append(i)

        return quick_sort(left)+middle_n+quick_sort(right)

nums = quick_sort(n)

print(nums)

if len(nums)%2!=0:
    middle = len(nums)//2
    result = nums[middle]

else:
    size = len(nums)
    print(size)
    m1 = size//2
    m2 = m1-1
    print(m1)
    print(m2)
    middle = nums[m1]+nums[m2]
    print(middle)
    result = middle / 2

print(result)



