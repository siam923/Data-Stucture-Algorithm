import math

## Implementation of the algorithm from slide DP_Change
def coin_change(coins, amount):

    d = len(coins)
    # Initialization
    cost_table = [math.inf for _ in range(amount+1)]
    prev = [0 for _ in range(amount+1)]


    cost_table[0] = 0

    for i in range(0, amount+1):
        for j in range(d):
            if (i>=coins[j]) and (cost_table[i-coins[j]] + 1 < cost_table[i]):
                cost_table[i] = cost_table[i-coins[j]] + 1
                prev[i] = coins[j]

    # if amount is less then coins
    if cost_table[1] == math.inf:
        return -1

    i = amount
    min_coins = []

    # Printint the coins 
    while i>0:
        print(prev[i])
        min_coins.append(prev[i])
        i = i - prev[i]

    return len(min_coins)




print("Enter Amount:")
amount = int(input().strip())

print("Enter coins seperated by space: ")
coins = list(map(int, input().rstrip().split()))


coin_change(coins, amount)
