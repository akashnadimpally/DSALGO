import string
from math import ceil
from itertools import permutations


coupon = "bcaa"
k = 3
# print(coupon[1:k+1:1])

alphabet = list(string.ascii_lowercase)

print(alphabet)

print(list(coupon))

d = {}

for i in range(1,27):
    d[alphabet[i-1]] = i

print(d)

parts = [coupon[j:j+k:1] for j in range(0, len(coupon))]


# stride = ceil(len(coupon) / k)
# parts = [coupon[i:i+stride] for i in range(0, len(coupon), stride)]
# print(parts)


print(parts)

val = []

for x in parts:
    print(x)
    f = {i: x.count(i) for i in set(x)}
    print(f)
    sum_c = 0
    for g in x:
        sum_c += d[g]**f[g]
    print(sum_c)
    val.append(sum_c)

print(val)

