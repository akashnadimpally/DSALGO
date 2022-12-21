b1 = [[1, 3],[2, 2],[3, 1]]
# b1 = [[5, 10], [2, 5], [4, 7], [3, 9]]
# trucksize = 9
trucksize = 4

# Greedy Algo
b1.sort(key= lambda r: (r[1]), reverse=True)
print(b1)
total_units = 0
for numboxes, units in b1:
    if trucksize <= numboxes:
        total_units += trucksize * units
        break

    total_units += numboxes * units
    trucksize -= numboxes

print(total_units)