# # s = "hello"

# # v = []
# # pos = []
# # d = {}

# # vowels = ['a','e','i','o','u']

# # for i in range(0,len(s)):
# #     if s[i] in vowels:
# #         pos.append(s[i])
# #         v.append(i)
# #         d[s[i]] = i

# # print(pos)
# # print(v)
# # print(d)

# # rev_pos = []

# # for j in range(len(pos)-1,-1,-1):
# #     rev_pos.append(pos[j])

# # print(rev_pos)


# s = "hello"

# vowels = ['a','e','i','o','u']

# t = s.lower()

# a = []

# for i in t:
#     if i in vowels:
#         a.append(ord(i))

# print(a)

# # print(chr(101))

# temp = a

# a[0],a[1] = a[1],a[0]

# b = a

# print(b)

s = list("hello")
# t = s.lower()
vowels = ['a','e','i','o','u','A','E','I','O','U']

n = len(s)

l = 0
r = n-1

while (l<r):
    while (l<n and (s[l] not in vowels)):
        l+=1
    while (r>=0 and (s[r] not in vowels)):
        r-=1
    if (l>=r):
        break

    s[l],s[r] = s[r],s[l]
    l+=1
    r-=1


print(''.join(s))