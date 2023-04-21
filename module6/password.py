"""
Write a program that prompts a user for a password.
Validates the passwords on some requirements.
Keeps prompting the user for a better password if the password does not meet the requirements.

Requirements:
Passwords must contain at least eight characters and no more than 128 characters.
Passwords must contain at least one uppercase letter.
Passwords cannot contain words connected to Texas A&M culture, including but not limited to aggie, whoop, hullabaloo, bonfire, and reveille.
"""

trials = 1
password = input("Enter your TAMU password: ")

# Validation
valid_length = 8 <= len(password) <= 128

contains_uppercase = False
for character in password:
    if character.isupper():
        contains_uppercase = True
        break

contains_aggie_words = False
aggie_words = ["aggie", "whoop", "hullabaloo", "bonfire", "reveille"]
for word in aggie_words:
    if word in password.lower():
        contains_aggie_words = True
        break

valid_password = valid_length and contains_uppercase and not contains_aggie_words

print(f"Valid length: {valid_length}")
print(f"Contains uppercase: {contains_uppercase}")
print(f"Contains no aggie words: {not contains_aggie_words}")
print(f"Is the password valid? {valid_password}")

while not valid_password:
    # Keep asking and verify again
    trials += 1
    password = input("\nEnter your TAMU password again: ")

    # Validation
    valid_length = 8 <= len(password) <= 128

    contains_uppercase = False
    for character in password:
        if character.isupper():
            contains_uppercase = True
            break

    contains_aggie_words = False
    aggie_words = ["aggie", "whoop", "hullabaloo", "bonfire", "reveille"]
    for word in aggie_words:
        if word in password.lower():
            contains_aggie_words = True
            break

    valid_password = valid_length and contains_uppercase and not contains_aggie_words

    print(f"Valid length: {valid_length}")
    print(f"Contains uppercase: {contains_uppercase}")
    print(f"Contains no aggie words: {not contains_aggie_words}")
    print(f"Is the password valid? {valid_password}")

print(f"You choose a valid password {password} after {trials} trials")