s = "Let's take LeetCode contest"

k = s.split(' ')

n = len(k)

l = 0
r = n - 1
while(l<r):
    k[l], k[r] = k[r], k[l]
    l , r = l+1, r-1
    

print(k)
t = []

for i in k:
    temp = i[::-1]
    t.append(temp)

print(t)

ans = ' '.join(t)

print(ans)