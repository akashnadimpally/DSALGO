def quick_sort(l: list[int]) -> list[int]:
    n = len(l)
    if n<=1:
        return l
    else:
        pivot = l.pop()
    
    left = []
    right = []
    for i in l:
        if i > pivot:
            right.append(i)
        else:
            left.append(i)
    return quick_sort(left)+[pivot]+quick_sort(right)


def binary_search(l: list[int],s: int):
    t = quick_sort(l)
    print(t)
    n = len(t)
    lower = 0
    higher = n-1
    while (lower <= higher):
        mid = (lower+higher)//2
        if (t[mid] > s):
            higher = mid - 1
        elif (t[mid] < s):
            lower = mid + 1
        else:
            return mid
        
    return -1

l = [2,5,3,7,4,88,33,40]
s = 33
print(binary_search(l,s))


