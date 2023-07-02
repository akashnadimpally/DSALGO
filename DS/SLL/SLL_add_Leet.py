r1 = [2,4,3]
r2 = [5,6,4]


def reverseList(r) -> list:
    length = len(r)
    krev = []
    for i in range(length-1, -1, -1):
        krev.append(str(r[i]))
    return krev


m1 = reverseList(r1)
m2 = reverseList(r2)

print(m1)
print(m2)

c1 = ''.join(m1)
c2 = ''.join(m2)

c = int(c1)+int(c2)

# print(c)

temp = str(c)

p = []

d = len(temp)

for i in range(d-1,-1,-1):
    p.append(int(temp[i]))

print(p)





#
# r1 = ['2','4','9']
# r2 = ['5','6','4','9']
#
# n1 = len(r1)
# n2 = len(r2)
#
# res = []
#
# m1 = int(''.join(r1))
# m2 = int(''.join(r2))
#
# res = str(m1+m2)
#
# print(res)
#
# k = len(res)
# p = []
# for i in range(k-1,-1,-1):
#     p.append(res[i])
#
#
# print(p)





