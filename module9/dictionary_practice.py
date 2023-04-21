"""
A dictionary is an unordered collection of elements.
A dictionary is a mapping between the keys and a set of values, which are mutable.
Each key maps to a value. The association of a key and a value is called a key-value pair.
"""
import string

declaration_of_independence = "We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.--That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, --That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness. Prudence, indeed, will dictate that Governments long established should not be changed for light and transient causes; and accordingly all experience hath shewn, that mankind are more disposed to suffer, while evils are sufferable, than to right themselves by abolishing the forms to which they are accustomed. But when a long train of abuses and usurpations, pursuing invariably the same Object evinces a design to reduce them under absolute Despotism, it is their right, it is their duty, to throw off such Government, and to provide new Guards for their future security.--Such has been the patient sufferance of these Colonies; and such is now the necessity which constrains them to alter their former Systems of Government. The history of the present King of Great Britain is a history of repeated injuries and usurpations, all having in direct object the establishment of an absolute Tyranny over these States. To prove this, let Facts be submitted to a candid world."
# Remove all the punctuations from the paragraph
print(f"Before punctuations removal: {declaration_of_independence}")

for punctuation in string.punctuation:
    declaration_of_independence = declaration_of_independence.replace(punctuation, '')

print(f"\nAfter punctuations removal: {declaration_of_independence}")

# Create a dictionary that holds all words
# book = {}
book = dict()
declaration_of_independence = declaration_of_independence.split()
print(f"\nAfter words split: {declaration_of_independence}")

for word in declaration_of_independence:
    print(word)
    # Update the count if the word is already in the dictionary
    if word not in book:
        # Add a word to the dictionary book (OPTION 1)
        # Create an item {word:word_count} to add to the dictionary book
        # An item is {key:value} pair
        # entry = {word: 1} # Map the count of 1 to the key 'word'
        # book.update(entry) # Add an item to the dictionary

        # Add a word to the dictionary book (OPTION 2)
        book[word] = 1 # Map the count of 1 to the key 'word', Add an item to the dictionary
    elif word in book:
        book[word] += 1 # Increment the value mapped to the key 'word'

print(f"\nThe dictionary of words is: {book}")
print(f"\nThe keys in the book dictionary of words are: {book.keys()}")
print(f"\nThe values in the book dictionary of words are: {book.values()}")
print(f"\nThe items in the book dictionary of words are: {book.items()}")

# get the word with the minimum count
max_value = max(book, key=book.get)
print(f"The word with the maximum count is: {max_value}")

# Iterating over the dictionary of books
# When iterating over a dictionary, the iterator is a key
for n in book:
    print(f"{n}")

# Print the words count in the declaration of independence in a formatted table
print(f"\nDeclaration of independence word count".upper())
print(f"{'Word':^20}{'Word Count':^20}")
for word in book:
    # Row printing option 1
    # print(f"{word:^20}{book[word]:^20}")

    # Row printing option 2
    print(f"{word:<20}{book.get(word):^20}")

# Summary
# There are two ways to write a value in a dictionary
print(f"Way 1: Set the word count of Government to 6")
book['Government'] = 6

print(f"Way 2: Set the word count of Government to 6")
entry = {'Government': 6}
book.update(entry)

# There are two ways to read a value from a dictionary
print(f"Way 1: The value associated to Government {book['Government']}")
print(f"Way 2: The value associated to Government {book.get('Government')}")

