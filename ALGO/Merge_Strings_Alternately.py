word1 = "abc"
word2 = "pqr"
n1 = len(word1)
n2 = len(word2)

w = word1+word2
n = len(w)
# print(w)
res = ""

i = 0
j = 0

while i<n1 and j<n2:
    res += word1[i] + word2[j]
    i+=1
    j+=1
while i<n1:
    res += word1[i]
    i+=1
while j<n2:
    res += word2[j]
    j+=1

print(res)