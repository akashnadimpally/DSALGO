arr = [0,2,10,0]

max_value = arr[0]
for i in arr:
    if max_value < i:
        max_value = i

print(arr.index(max_value))