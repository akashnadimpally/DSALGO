# s = "cbbd"
s = "ccc"
res = [s[i:j] for i in range(len(s))
       for j in range(i+1, len(s)+1)]

m = len(s)
if m<=1:
    print(s)

def Palindrome(ans):
    rev = ans[::-1]
    # print("ans: "+ans)
    # print("rev: "+rev)
    if rev == ans:
        return True
    else:
        return False

print(res)
d = {}
y = {}
b = None
for i in res:
    n = len(i)
    if n>=2:
        k = Palindrome(i)
        if k:
            b = i
            # d[i] = len(i)
            # y[k] = len(i)

if b is None:
    print(s[0])
else:
    print(b)
# print(d)
# print(y)