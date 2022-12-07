x = 121

lx = list(str(x))
lr = []
print(lx)
n = len(lx)
for i in range(n-1,-1,-1):
    lr.append(lx[i])

if lx == lr:
    print("Palindrome")