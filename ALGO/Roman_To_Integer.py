s = 'MCMXCIV'

d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'O': 0}

c = 0

r = s+'O'

print(r)

roman_list = list(r)

print(roman_list)

n = len(roman_list)

c = 0

for i in range(0,n-1):
    print(i)
    print(d[roman_list[i]])
    print(d[roman_list[i+1]])
    if d[roman_list[i]] >= d[roman_list[i+1]]:
        c += d[roman_list[i]]
    else:
        c -= d[roman_list[i]]

print(c)


# i=0
# while(i<=n):
#     print(d[roman_list[i]])
#     print(d[roman_list[i+1]])
#     if d[roman_list[i]] >= d[roman_list[i+1]]:
#         c += d[roman_list[i]]
#     else:
#         c -= d[roman_list[i]]
    
#     i+=1

# print(c)

# for i in range(0,n):
#     print(i)
#     print(d[roman_list[i]])
#     print(d[roman_list[i+1]])
#     if d[roman_list[i]] > d[roman_list[i+1]]:
#         c += d[roman_list[i]]
#     else:
#         c -= d[roman_list[i]]

# print(c)

# i=0
# while(i<=n):
#     if d[roman_list[i]] > d[roman_list[i+1]]:
#         c += d[roman_list[i]]
#     else:
#         c -= d[roman_list[i]]

# print(c)
