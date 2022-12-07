
def binary_search(l, target):
    low = 0
    high = len(r) - 1

    while (high >= low):
        mid = (low + high) // 2
        if (r[mid] > target):
            high = mid - 1
        elif (r[mid] < target):
            low = mid + 1
        else:
            return mid

    return -1


l = [1,31,51,3,5,6,24,76,21,86]

r = sorted(l)
target = 3
print(binary_search(r,target))