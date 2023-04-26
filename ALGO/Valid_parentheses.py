s = "(){}}{"

d = {'(':')', '[':']', '{':'}', ')':'(', ']':'[', '}':'{' }

open_l = ['(', '[', '{']
closed = [')', ']', '}']

# def ValidP(s):
#     p = list(s)
#     n = len(p)

#     k = []

#     for i in p:
#         if i in open:
#             k.append(i)
#         else:
#             if k[-1] == d[p[i]]:
#                 k.remove(i)
#             else:
#                 return False
#     return True


# print(ValidP(s))



def ValidP(s):
    p = list(s)
    n = len(p)

    if n == 1:
        return False
    
    if n == 2:
        for i in p:
            if d[i] in p:
                return True
            else:
                return False

    c = 0

    for i in p:
        if i in open_l:
            c += 1
        else:
            c -= 1


    for i in range(0,n-1):

        if p[i] in open_l:
            if p[i+1] in open_l:
                continue
            else:
                if p[i+1] == d[p[i]]:
                    for i in p:
                        print(i)
                        if d[i] in p:
                            p.remove(d[i])
                            continue
                        else:
                            return False
                    # break
                    return True
                else:
                    return False
        
        # elif p[i] in closed:
        #     return False

        else:
            if d[p[i]] not in p:
                return False
    
    return True


        # if p[i+1] == d[p[i]]:
        #     for i in p:
        #         print(i)
        #         if d[i] in p:
        #             p.remove(d[i])
        #             continue
        #         else:
        #             return False
        #             # break
        #     return True
        # else:
        #     return False


print(ValidP(s))

# p = list(s)
# n = len(p)

# for i in range(0,n-1):
#     if p[i+1] == d[p[i]]:
#         for i in p:
#             print(i)
#             if d[i] in p:
#                 p.remove(d[i])
#                 continue
#             else:
#                 print('False')
#                 break
#         print('True')
#     else:
#         print('False')


# for i in p:
#     print(i)
#     if d[i] in p:
#         p.remove(d[i])
#         continue
#     else:
#         print('False')
#         break
    
# print('True')