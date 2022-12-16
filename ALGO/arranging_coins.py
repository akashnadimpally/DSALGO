import math

n = 8


# Method - 1

k = math.sqrt(2*n+0.25) - 0.5

print(int(k))

# Binary Search - Method - 2

low, high = 0, n
while low <= high:
    k = (high + low) // 2
    curr = k * (k + 1) // 2
    if curr == n:
        print(k)
    if n < curr:
        high = k - 1
    else:
        low = k + 1


print(high)