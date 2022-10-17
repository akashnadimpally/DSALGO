

def quick_sort(l):
    n = len(l)
    if n <= 1:
        return l
    else:
        pivot = l.pop()

    l_lower = []
    l_higher = []

    for i in l:
        if i > pivot:
            l_higher.append(i)
        else:
            l_lower.append(i)
    return quick_sort(l_lower) + [pivot] + quick_sort(l_higher)


f = [2,3,652,5,2,5,2,76,8,2,5,3,7,2,7,9,4345,2,-331,435,23]
print(quick_sort(f))