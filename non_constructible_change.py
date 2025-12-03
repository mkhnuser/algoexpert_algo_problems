def nonConstructibleChange(coins):
    change = 1

    if not coins:
        return change

    change = 0

    coins.sort()

    for coin in coins:
        change += coin


if __name__ == "__main__":
    nonConstructibleChange([1, 2, 5])  # 4
    nonConstructibleChange([])  # 1
