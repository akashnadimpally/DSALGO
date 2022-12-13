from math import sqrt

num = 14

# temp = (num)**(1/2)
#
#
# print(temp)
# q = int((num+1)/2)
# for i in range(q):
#     u = i*i
#     print(str(i)+" -> "+str(u))
#     if float(i) == temp:
#         print(True)
#         break
#
# s = sqrt(num)
# print(s)

temp = int((num)**(0.5))

if temp**2 == num:
    print(True)
else:
    print(False)