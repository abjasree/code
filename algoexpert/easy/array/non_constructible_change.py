def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    current_change = 0
    for coin in coins:
        if coin > current_change + 1:
            return current_change + 1
        current_change += coin
    return current_change + 1
