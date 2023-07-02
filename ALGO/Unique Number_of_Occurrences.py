arr = [1,2,2,1,1,3]

l = list(set(arr))
d = {}
s = []

for i in l:
    c = 0
    for j in arr:
        if i == j:
            c += 1
    s.append(c)
    d[i] = c


n1 = len(s)
t = set(s)
n2 = len(t)

if n1 == n2:
    print(True)
else:
    print(False)

    