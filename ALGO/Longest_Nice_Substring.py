s = "c"
s = "cChH"

temp_s = list(s)

n = len(temp_s)

res = []


for k in range(0,n+1):
    for i in range(n-k+1):
        print(temp_s[i:i+k])
        c = temp_s[i:i+k]
        # w = len(list(set(c)))
        w = len(list(c))
        b = len(c)
        if w == b:
            res.append(''.join(c))
            # res.append(c)
        else:
            continue


print(res)

ans = []

for a in res:
    y = a.lower()
    v = len(list(set(list(y))))
    if v == 1:
        ans.append(a)

print(ans)

max_len_string = len(ans[0])
d = {}

for g in ans:
    d[g] = len(g)

print(d)



sol = max(d, key=lambda k: d[k])

if len(sol) > 1:
    print(sol)

else:
    print("")

# print(sol)






