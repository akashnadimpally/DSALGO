def SubArray(l):
    lists = []
    for i in range(len(l)+1):
        for j in range(i):
            lists.append(l[j:i])
    # p = []
    # for k in lists:
    #     g = sum(k)
    #     p.append(g)
    #
    # # return max(p)
    return lists

e = [1,2,3]
print(SubArray(e))


# l = [-1]
# t = SubArray(l)
# s = []
# for i in t:
#     g = sum(i)
#     s.append(g)
#
# print(max(s))