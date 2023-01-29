def knapsack(W, values, weights):
    ratios = [p / w for p, w in zip(values, weights)]
    n = len(ratios)
    index = list(range(n))
    arr = []

    for i in range(n):
        arr.append([ratios[i], weights[i], values[i]])

    arr.sort(reverse=True)

    max_value = 0
    fractions_obj = 0

    for i in range(n):
        if W > 0 and arr[i][1] < W:
            W -= arr[i][1]
            max_value += arr[i][2]
        else:
            fractions_obj = i
            break

    if W > 0:
        max_value += W*(arr[fractions_obj][2]/arr[fractions_obj][1])

    return int(max_value)




values = [10,5,15,7,6,18,3]
weights = [2,3,5,7,1,4,1]
m = 15

print(knapsack(m, values, weights))

