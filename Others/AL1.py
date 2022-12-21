s = 'MCMXCIV'
output = 1994

d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

roman = list(s)
Integer = 0
for i in roman:
    res = d[i]
    Integer += res

print(Integer)
