s = "egg"
t = "add"

output = []
lookup = {}

sd = {i: s.count(i) for i in set(s)}
td = {j: t.count(j) for j in set(t)}

print(sd)
print(td)

i = 1

for w in s:
    if w not in lookup:
        lookup[w] = i
        i+=1
    output.append(lookup[w])

print(output)



