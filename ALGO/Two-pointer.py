s = ["h","e","l","l","o"]
n = len(s)
t = []

# s = s[::-1]

# print(s)

l = 0
r = n-1

while(l<r):
    s[l], s[r] = s[r], s[l]
    l , r = l+1, r - 1

print(s) 