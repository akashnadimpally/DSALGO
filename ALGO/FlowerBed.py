def FlowerBed(bed, n):
    length = len(bed)
    c = 0

    for i in range(length):
        if (bed[i] == 0):
            left = (i == 0) or (bed[i-1] == 0)
            right = (i == bed[length - 1]) or (bed[length + 1] == 0)

            if left and right:
                bed[i] = 1
                c+=1
                if c>=n:
                    return True
    

bed = [1,0,0,0,1]
n = 1
print(FlowerBed(bed, n))