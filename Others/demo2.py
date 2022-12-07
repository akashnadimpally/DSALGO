def func(n):
    l = len(n)
    ls = 0
    rs = 0
    for i in range(0, l):
        if i == 0:
            ls = sum(n[:i])
            rs = sum(n[i+1:])
            print("------------------")
            print(i)
            print("ls")
            print(n[:i])
            print("rs")
            print(n[i+1:])
            print(ls)
            print(rs)
            if ls == rs:
                return i

        elif i == l - 1:
            ls = sum(n[:i])
            rs = sum(n[i:])
            print("------------------")
            print(i)
            print("ls")
            print(n[:i])
            print("rs")
            print(n[i:])
            print(ls)
            print(rs)
            if ls == rs:
                return i

        else:
            ls = sum(n[:i])
            rs = sum(n[i+1:])
            print("------------------")
            print(i)
            print("ls")
            print(n[:i])
            print("rs")
            print(n[i+1:])
            print(ls)
            print(rs)
            if ls == rs:
                return i

    return -1

n = [-1,-1,0,1,1,0]

print(func(n))


# #ls
# print(n[:1])
#
# #rs
# print(n[2:])
#
# print(sum(n[:1]))
# print(sum(n[2:]))

