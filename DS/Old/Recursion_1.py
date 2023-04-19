# def binary_recursion(n, target):
#     r = sorted(n)
#     low = 0
#     high = len(r)-1
#     res = helper(r,low,high,target)
#     return res

# Recursion
def binary_search(n, low, high, target):
    if (low <= high):
        mid = (low+high)//2
        if (n[mid] > target):
            high = mid - 1
            helper(n, low, high, target)
        elif (n[mid] < target):
            low = mid + 1
            helper(n, low, high, target)
        else:
            return mid
    else:
        return -1


l = [0,13,45,14,31,42,-3,41]
target = -3
r = sorted(l)
print(r)
low = 0
high = len(r)-1
print(binary_search(l, low, high, target))