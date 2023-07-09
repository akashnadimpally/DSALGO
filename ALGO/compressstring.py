# chars = ["a","a","b","b","c","c","c"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

t = list(set(chars))

n = len(t)

if n > 1:
    print(n*2)
else:
    print(n)