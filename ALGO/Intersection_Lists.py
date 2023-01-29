arr1 = [197,418,523,876,1356]
arr2 = [501,880,1593,1710,1870]
arr3 = [521,682,1337,1395,1764]

# t = []
#
# for i in arr1:
#     if i in arr2:
#         if i in arr3:
#             t.append(i)
#
# print(t)

print(sorted(set(arr1) & set(arr2) & set(arr3)))