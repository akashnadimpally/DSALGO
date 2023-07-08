# candies = [2,3,5,1,3]
# extraCandies = 3

candies = [2,8,7]
extraCandies = 1

p = []
res = []

for i in candies:
    s = i + extraCandies

    if len(p) == 0:
        k = 0
    else:
        k = max(p)

    # if s >= k:
    #     res.append(True)
    # else:
    #     res.append(False)
    p.append(s)

e = p[0]

for i in p:
    if i>= e:
        res.append(True)
    else:
        res.append(False)

# i = 0
# while (i < len(candies)):
#     s = candies[i] + extraCandies

#     k = max


print(p)
print(res)