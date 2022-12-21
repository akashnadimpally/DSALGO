b1 = [[1, 3],[2, 2],[3, 1]]
# b1 = [[5, 10], [2, 5], [4, 7], [3, 9]]
# trucksize = 9
trucksize = 4


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





# s = []
#
# for i in range(0, len(b)):
#     for j in range(0, len(b[0]) - 1):
#         t = b[i][j] * b[i][j+1]
#         s.append(t)
#
# print(s)


# Sort the box types
# b.sort(key = lambda x: -x[1])
#
# capacity = 0
#
# for box, unit in b:
#     if trucksize < box:
#         trucksize -= box
#         capacity += box*unit
#     else:
#         capacity += trucksize*unit
#         break
#
# print(capacity)