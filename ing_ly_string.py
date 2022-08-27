# ing_ly_string.py
# written by DeAnna

from tomlkit import string

# declaring variables
given_result = string(' ')

# name of function


def inglyString():

    # user given input string
    given_string = str(input("Enter your word:  "))
    if len(given_string) < 3:
        print(given_string)
        return given_string
    if given_string.endswith("ing"):
        given_result = (given_string + "ly")
        print(given_result)
        return given_result
    else:
        given_result = (given_string + "ing")
        print(given_result)
        return given_result


# This is where the function is called.
inglyString()
