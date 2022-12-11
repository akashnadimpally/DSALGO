import string


def solution(letters, target):

    for c in letters:
        if c > target:
            return c
    return letters[0]

    # alphabets = list(string.ascii_lowercase)
    # letters_set = sorted(list(set(letters)))
    # index_t = alphabets.index(target)
    # d = {}
    #
    # for i in range(0, len(letters_set)):
    #     d[letters_set[i]] = alphabets.index(letters_set[i])
    #
    # print(d)
    #
    # d_values = [v for k, v in d.items()]
    #
    # low = 0
    # high = len(d_values) - 1
    # x = binary_search(d_values, low, high, index_t)
    #
    # print(x)
    #
    # for k,v in d.items():
    #     print(v)
    #     if v>d_values[x]:
    #         return k



def binary_search(nums, low, high, target):

    if (target in nums):
        if (high >= low):
            mid = (low + high) // 2
            if (nums[mid] > target):
                high = mid - 1
                return binary_search(nums, low, high, target)
            elif (nums[mid] < target):
                low = mid + 1
                return binary_search(nums, low, high, target)
            else:
                return mid
    else:
        nums.append(target)
        r = sorted(nums)
        low_r = 0
        high_r = len(r) - 1
        return binary_search(r, low_r, high_r, target)


letters = ['c', 'f', 'j']
# letters = ['x','x','y','y']
target = 'c'


# print(binary_search(letters, target))

print(solution(letters, target))
