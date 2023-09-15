n = 9669

s = list(str(n))
k = []
print(s)

for i in range(0,len(s)):
    temp = s
    if temp[i] == '6':
        s[i] = '9'
    t = ''.join(s)
    k.append(t)

print(k)