# s = "the sky is blue"

s = "a good   example"

t = s.split(" ")

print(t)

res = []

for i in range(len(t)-1,-1,-1):
    if len(t[i]) > 0:
        res.append(t[i])


print(res)
print((' '.join(res)).strip())
