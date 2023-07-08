gain = [-5,1,5,0,-7]
res = []
c = 0

gain.insert(0,0)

print(gain)

for i in gain:
    c = c + i
    res.append(c)

print(res)
