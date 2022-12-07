def sample(n):
    if n > 0:
        return n + sample(n-1)
    else:
        return 0


n = 4
print(sample(n))