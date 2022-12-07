s = "egg"
t = "add"

ns = len(s)
nt = len(t)
s1 = list(s)
t1 = list(t)

ds = {}
dt = {}

# print(set(s))
# print(set(t))

if (ns == nt):
    ds = {i: s.count(i) for i in set(s1)}
    dt = {j: t.count(j) for j in set(t1)}
    print(ds)
    print(dt)
    ds_values_sorted = sorted(ds.values())
    dt_values_sorted = sorted(dt.values())
    print(ds_values_sorted)
    print(dt_values_sorted)
    if ds_values_sorted == dt_values_sorted:
        print(True)
    else:
        print(False)

else:
    print(False)

