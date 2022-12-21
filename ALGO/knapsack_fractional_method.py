p = [10,5,15,7,6,18,3]
w = [2,3,5,7,1,4,1]
m = 15

p_w = []

n = len(p)

for i in range(0,n):
    t = p[i]/w[i]
    p_w.append(t)

print(p_w)


for j in w:
    while j<=m:
        m -= j
        