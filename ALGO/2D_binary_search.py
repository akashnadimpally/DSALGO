def binary_search(num, target):
    low = 0
    high = len(num)
    if target in num:
        while(low<=high):
            mid = (low+high)//2
            # print(mid)
            if target < num[mid]:
                high = mid - 1
            elif num[mid] < target:
                low = mid + 1
            else:
                return mid
    else:
        return -1



matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

m = len(matrix)
n = len(matrix[0])

# print(len(matrix))

for i in range(len(matrix)):
    r = sorted(matrix[i])
    t = binary_search(r, target)
    print(t)
    # if t != -1:
    #     print(str(i)+" X "+str(t))


