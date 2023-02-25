nums = [-3,-2,-1,0,0,1,2]

p = []
n = []

for i in nums:
    if i>0:
        p.append(i)
    elif i<0:
        n.append(i)
    else:
        continue

Pn = len(p)
Nn = len(n)

if Pn > Nn:
    print(Pn)
else:
    print(Nn)