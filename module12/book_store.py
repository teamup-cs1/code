import random

import book_library


def print_books(bookstore):
    """
    Print two versions of the dictionaries containing book records

    @param bookstore: the group of books to manage
    @return:
    """
    # Types of bookstore
    # 1 bookstore = {ISBN1: [title, -1], ISBN2: [title, 2], ISBN3: [title, 8], ISBN4: [title, 6],
    # ISBN5: [title, 2], ISBN6: [title, -1]}
    # 2 bookstore = {ISBN1: [title, -1, price], ISBN2: [title, 2, price],
    # ISBN3: [title, 8, price], ISBN4: [title, 6, price], ISBN5: [title, 2, price], ISBN6: [title, -1, price]}
    for ISBN, record in bookstore.items():
        if len(bookstore[ISBN]) == 2:
            print(f"{'ISBN:':<6}{ISBN:<11}{'Title:':<7}{record[0]:<20}{'Collection:':<12}{record[1]:<4}")
        elif len(bookstore[ISBN]) == 3:
            print(f"{'ISBN:':<6}{ISBN:<11}{'Title:':<7}{record[0]:<20}{'Collection:':<12}{record[1]:<4}{'Price:':<7}{round(record[2], 20):<6}")


def set_prices(starting_price, ending_price, bookstore):
    """
    This function adds a price record to the dictionary of books

    @param starting_price: The starting price of books in the bookstore
    @param ending_price: The ending / maximum price of books in the bookstore
    @param bookstore: The bookstore dictionary
    @return: None
    """
    for ISBN, record in bookstore.items():
        price = random.uniform(starting_price, ending_price)
        bookstore[ISBN].append(price)


def main():
    """
    This is the entry point to the bookstore
    @return:
    """
    bookstore = {}
    while True:
        book_library.print_menu()
        option = int(input("Enter an option: "))
        if option == 1:
            book_library.add_books(bookstore)
        elif option == 2:
            print_books(bookstore)
        elif option == 8:
            starting_price = float(input("Starting price: "))
            ending_price = float(input("Ending price: "))
            set_prices(starting_price, ending_price, bookstore)


main()
