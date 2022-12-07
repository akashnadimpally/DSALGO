s = "acb"
t = "ahbgdc"
sl = list(s)
tl = list(t)
print(sl)
print(tl)
n = len(sl)
c = 0
# for i in sl:
#     if i in tl:
#         c = c+1
#     else:
#         break

for i in sl:
    print("Printing i value ------------------")
    print(i)

    for j in tl:
        print("Printing j value ------------------")
        print(j)

        if i == j:
            print("i and j values matched")
            c = c+1
            print("Printing c value ------------------")
            print(c)

            # break
        # else:
        #     break


if c == n:
    print(True)
else:
    print(False)