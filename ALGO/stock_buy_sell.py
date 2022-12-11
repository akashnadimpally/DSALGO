# prices = [7,1,5,3,6,4]
prices = [2,4,1]

# pivot = min(prices)
feasible = []


# for i in range(0,len(prices)):
#     if (pivot < prices[i]) and (prices.index(pivot) < i):
#         profit = prices[i] - pivot
#         feasible.append(profit)


# feasible.sort(reverse=True)
# print(feasible)

# b = None
#
# for i in feasible:
#     if b is None or b < i:
#         b = i
#
# print(b)

# Brute Force

# max_profit = 0
#
# for i in range(len(prices) - 1):
#     for j in range(i+1, len(prices)):
#         profit = prices[j] - prices[i]
#         if profit > max_profit:
#             max_profit = profit
#
# print(max_profit)

# One Pass - Greedy Algorithm

min_price = float('INF')
max_profit = 0

for i in range(len(prices)):
    if prices[i] < min_price:
        min_price = prices[i]
    elif prices[i] - min_price > max_profit:
        max_profit = prices[i] - min_price

print(max_profit)