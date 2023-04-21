price = 100 # This is global variable


def store1():
    """This is the first store"""
    #price = 20 # Local variable
    global price
    price = price + 6
    print(f"The price in store 1 is {price}")
    price += 10
    print(f"The price in store 1 is {price}")


def store2():
    """This is the second store"""
    price = 60 # Local variable
    print(f"The price in store 2 is {price}")
    price += 100
    print(f"The price in store 2 is {price}")


store1()
store2()
print(price)
