prices = [7,6,4,3,1]

profits = []

n = len(prices)

# for i in range(0,n):
#     for j in range(i+1,n):
#         if prices[i] < prices[j]:
#             prof = prices[j] - prices[i]
#             profits.append(prof)

# if len(profits) == 0:
#     print(0)
# else:
#     print(max(profits))

if n == 0:
    print(0)
else:
    min_value = prices[0]
    max_profit = 0

for i in range(1,n):
    if prices[i] < min_value:
        min_value = prices[i]
    else:
        max_profit = max(max_profit, prices[i] - min_value)

print(max_profit)