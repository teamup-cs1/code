denominations = [['dollar', 100], ['quarter', 25], ['dime', 10], ['nickel', 5], ['cent', 1]]

amount = 5.89 * 100
remainder = amount

for denomination in denominations:
    count = remainder // denomination[1]
    remainder = remainder % denomination[1]

    print(f"\nNumber of {denomination[0]}: {count}")
    print(f"The remainder is {remainder}")
