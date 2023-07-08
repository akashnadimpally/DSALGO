# str1 = "ABABAB"
# str2 = "ABAB"

str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"

len_str1 = len(str1)
len_str2 = len(str2)

temp = str1

if len_str1 > len_str2:
    str1 = str1
    str2 = str2

else:
    str1 = str2
    str2 = temp

print(str1)
print(str2)

n1 = len(str1)
n2 = len(set(str2))

m = min(n1,n2)

k = [str1[i:i+m] for i in range(0,n1,m)]

print(k)

c = 0
r = ''.join(sorted(list(set(str2))))

for i in k:
    print("i: "+i)
    print("r: "+r)
    if i == r:
        c += 1

print(c)

if c > 1:
    print(str2)
else:
    print("")