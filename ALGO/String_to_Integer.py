# def isfloat(num):
#     try:
#         float(num)
#         return True
#     except ValueError:
#         return False
#
#
# # s1 = "words and 987"
# # s1 = "-91283472332"
# s1 = "3.14159"
# t1 = "".join(s1.split())
# # print(t1)
#
# if t1.isalnum():
#     k = []
#     for i in t1:
#         if i.isnumeric():
#             k.append(i)
#         else:
#             break
#     result = "".join(k)
#
# else:
#     result = "".join(s1.split())
#
# # print(result)
# # print(type(result))
# # print(len(result))
#
# if len(str(result)) != 0:
#     if ((-2)**31) < float(result) < (((2)**31)-1):
#         if isfloat(result):
#
#
#     elif int(result) > 0:
#         print(((2)**31)-1)
#     elif int(result) < 0:
#         print((-2)**31)
#     else:
#         print(0)
# else:
#     print(0)


# s = "words and 987"
# s = "-91283472332"
# s = "3.14159"

s = "42"


INT_MIN = -2 ** 31
INT_MAX = 2 ** 31 - 1

s = s.strip()
if not s:
    print(0)

sign = -1 if s[0] == '-' else 1
if s[0] in ['-', '+']:
    s = s[1:]

res = 0
for i in range(len(s)):
    if s[i].isdigit():
        res = res * 10 + int(s[i])
    else:
        break

res *= sign
if res < INT_MIN:
    print(INT_MIN)
if res > INT_MAX:
    print(INT_MAX)

print(res)



