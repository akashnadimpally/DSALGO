def binary_search(l: list, s):
    begin_index = 0
    end_index = len(l) - 1

    while (begin_index <= end_index):
        midpoint_index = begin_index + (end_index - begin_index) // 2
        midpoint_value = l[midpoint_index]
        if midpoint_value == s:
            return midpoint_index
        elif s < midpoint_value:
            end_index = midpoint_index - 1
        else:
            end_index = midpoint_index + 1

    return None


l = [1,6,32,62,6,2,69,2,62,832,9]

print(binary_search(l,2))