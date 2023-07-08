s = "hello"

pos = []
d = {}

vowels = ['a','e','i','o','u']

for i in range(0,len(s)):
    if s[i] in vowels:
        pos.append(s[i])
        d[s[i]] = i

print(pos)
print(d)