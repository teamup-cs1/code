# File: book_library.py
# Author: Student name
# Date: xx/xx/2022
# Section: Student section number
# E-mail: student_email@tamu.edu
# Description:
# e.g., This program asks for ...

from math import *


def main():
    """Driver function"""
    library = {}  # This is the library of books
    while True:
        print_menu()
        option = input('Choose a menu option: ')
        if option == '1':
            add_books(library)
        elif option == '2':
            print_books(library)
        elif option == '3':
            create_collections(library)
        elif option == '4':
            sort_collections(library)
        elif option == '5':
            delete_collection(library)
        elif option == '6':
            print("End", end='')
            break
        else:
            print('\nInvalid entry\n')


def print_menu():
    """Prints the menu of options to the librarian"""
    # to do
    """Print the main menu of 6 options to the librarian"""
    print(f"*******************Main Menu*******************")
    print("1. Add books to the library")
    print("3. Create book collections")
    print("6. Quit")
    print("***********************************************")
    pass


def check_isbn(isbn):
    """Checks the format of an ISBN"""
    # to do
    pass


def isbn_in_library(library, ISBN):
    """This function checks if  a book is in the library
    
    @param library
    @param ISBN
    @return 
    """
    return ISBN in library
    pass


def isbn_is_valid(ISBN):
    """
    This function checks if an ISBN valid
    @param ISBN:
    @return: Boolean True is the ISBN is 10 digits long
    """
    return ISBN.isnumeric and len(ISBN) == 10


def add_books(library):
    """Adds unique books to the library"""
    # to do
    entries = int(input("How many books would you like to enter: "))
    for book in range(1, entries + 1):
        entry = input(f"Enter book {book}: ")
        ISBN = entry.split()[-1]
        title = entry[:-11].strip()
        # to do: Before adding the book to the library, check if the ISBN is valid and the book in not in the library...
        print(f"Is ISBN valid? {isbn_is_valid(ISBN)}")
        print(f"Is ISBN {ISBN} in the library? {isbn_in_library(library, ISBN)}")
        library[ISBN] = [title, -1]  # At insertion of a new book, initialize each book to a 'null' collection
    print(library)


def print_books(library):
    """Prints available books in the library"""
    # to do
    pass


def create_collections(library):
    """
    Creates a collection of books
    If the library has library_size books and the collection is collection_size, What is the number of collections?

    @param library:
    @return: None
    """
    # library = {ISBN1: [title, -1], ISBN2: [title, 2], ISBN3: [title, 8], ISBN4: [title, 6], ISBN5: [title, 2], ISBN6: [title, -1]}

    print(f"The keys (ISBN) in the library are {library.keys()}")
    print(f"The values ([title, collection]) in the library are {library.values()}")

    library_size = len(library)
    available_books = [library[ISBN][1] for ISBN in library.keys() if library[ISBN][1] == -1]
    print(f"List of available textbooks: {available_books}")
    number_of_available_books = len(available_books)
    print(f"The number of books in the library is: {library_size}")
    print(f"The number of available books in the library is: {number_of_available_books}")

    collection_size = int(input("What is the size of the collection?"))
    number_of_collections = ceil(number_of_available_books / collection_size)
    print(f"The number of collections is: {number_of_collections}")

    # Create a loop that repeats number_of_collections times and set the collection values to a collection number


def sort_collections(library):
    """Sort books in the collections"""
    # to do
    pass


def delete_collection(library):
    """Deletes a collection"""
    # to do
    pass


if __name__ == "__main__":
    main()  # Called only if the collections is running as standalone
