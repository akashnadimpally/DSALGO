x = 1534236469


if ((x>=(-2)**31) and (x<=((2**31)-1))):
    if x>=0:
        temp = str(x)
        # print(temp)
        f = temp[::-1]
        result = int(f)
    else:
        temp = str(x)
        q = temp[1:]
        f = q[::-1]
        result = int("-"+f)

    if ((result>=(-2)**31) and (result<=((2**31)-1))):
        print(result)
    else:
        print(0)
else:
    print(0)

print((-2)**31)
print((2**31)-1)
