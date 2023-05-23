s = "aababcabc"
k = 3

temp = list(set(list(s)))

print(temp)

temp_s = list(s)

for i in range(len(temp_s)-k+1):
    print(temp_s[i:i+k])


res = []

for i in range(len(temp_s)-k+1):
    r = temp_s[i:i+k]
    q = list(set(r))

    if len(q) == 3:
        e = ''.join(r)
        res.append(e)

    
print(len(res))



    

        
