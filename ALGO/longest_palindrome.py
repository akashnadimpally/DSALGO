import collections
from itertools import permutations, combinations
from datetime import datetime

start = datetime.now()


s = "tattarrattat"
n = len(s)

ans = 0
for v in collections.Counter(s).values():
    ans += v // 2*2
    if ans%2 == 0 and v%2 == 1:
        ans += 1

print(ans)

# s_combinations = [''.join(j) for i in range(n) for j in permutations(s,i+1)]
#
# print(s_combinations)
# d_values = []
# for k in s_combinations:
#     k_reverse = ''.join(reversed(k))
#     if (k == k_reverse):
#         d_values.append(len(k))



# for i in range(0,n):
#     t1 = s[i:]
#     t2 = s[:i]
#     permList1 = permutations(t1)
#     permList2 = permutations(t2)
#
#     for j in list(permList1):
#         q = ''.join(j)
#         q_reverse = ''.join(reversed(q))
#         if (q == q_reverse):
#             d_values.append(len(q))
#
#     for k in list(permList2):
#         q = ''.join(k)
#         q_reverse = ''.join(reversed(q))
#         if (q == q_reverse):
#             d_values.append(len(q))


# print(max(d_values))
end = datetime.now()

print(end - start)
