arr1 = [2,1,100,3]
arr2 = [-5,-2,10,-3,7]
d = 6

distance = []

res = 0
arr2.sort()
for i in range(0, len(arr1)):
    count = 0
    for j in range(0, len(arr2)):
        res = abs(arr1[i] - arr2[j])
        if not (res <= d):
            count += 1
        else:
            break
    if count == len(arr2):
        res += 1

print(res)


