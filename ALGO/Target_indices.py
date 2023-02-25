nums = [1,2,5,2,3]

target = 4

def quick_sort(n):
    left = []
    middle_n = []
    right = []

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

def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while (low<=high):
        mid = (low+high)//2
        if (nums[mid] > target):
            high = mid - 1
        elif (nums[mid] < target):
            low = mid + 1
        else:
            return mid


nums_main = quick_sort(nums)

print(nums_main)
result = binary_search(nums_main, target)

r = []

print(result)

for i in range(len(nums)):
    if result == None:
        r = []
    elif nums_main[result] == nums_main[i]:
        r.append(i)
    else:
        continue

print(r)