# Greedy Algo
denomination = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]

payment_made = 4368
amount_received = 10000
change = amount_received - payment_made
denoms = []
for d in denomination:
    while change >= d:
        change -= d
        denoms.append(d)

print(denoms)
print(sum(denoms))