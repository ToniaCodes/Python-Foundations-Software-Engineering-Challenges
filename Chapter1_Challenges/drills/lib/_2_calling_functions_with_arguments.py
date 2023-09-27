# == INSTRUCTIONS ==
#
# These challenges are a bit trickier and, in some cases, will require a few
# lines of code. If you start to get a little stuck, take a step back and make
# a plan by breaking the overall task down into small steps.

# == EXERCISES ==

# Purpose: checks if a string starts with the letter a
# Example:
#   Call:    starts_with_the_letter_a("apple")
#   Returns: True
#   Call:    starts_with_the_letter_a("Apple")
#   Returns: True
#   Call:    starts_with_the_letter_a("Rock")
#   Returns: False

# capital_A = A


def starts_with_the_letter_a(string):
    if string[0] == "a": 
        return True
    elif string[0] == "A":
        return True
    else:
        return False
    
    
# my initial attempt belwo for the above code:
# def starts_with_the_letter_a(string):
#     if (string)[0] == "a" or "A":
#         return ("True")
#     else:
#         return ("FALSE")
 

# take in input in the form of a string
    #Check to see what letter the string starts with
    #If the letter is a then python to return true
    #if the letter is false then python to return false
    #create a function that can take any input and check to see if the first letter is an a or A


    # your code goes here (delete the pass below)
    
#if the first letter in a string is = a

# Purpose: checks if a string ends with the letter a
# Example:
#   Call:    ends_with_the_letter_a("Java")
#   Returns: True
#   Call:    ends_with_the_letter_a("JAVA")
#   Returns: True
#   Call:    ends_with_the_letter_a("Python")
#   Returns: False
def ends_with_the_letter_a(string):
    if string[-1] == 'a':
        return True
    elif string[-1] == 'A':
        return True
    else:
        return False
    
# Purpose: checks if a string contains the word hello
# Example:
#   Call:    contains_hello("hello world")
#   Returns: True
#   Call:    contains_hello("HELLO WORLD")
#   Returns: True
#   Call:    contains_hello("world")
#   Returns: False
def contains_hello(string):
    if "Hello" in string:
        return True
    elif "hello" in string:
        return True
    else: 
        return False
    
    # if string == "Hello":
    #     return True
    # elif string == "HELLO":
    #     return True
    # else:
    #     return False
    
    



# Purpose: replaces the word hello with the word goodbye
# Note: you don't need to worry about matching 'Hello' or 'HELLO' here
#       lowercase only is fine.
# Example:
#   Call:    substitute_hello_with_goodbye("hello folks")
#   Returns: "goodbye folks"
#   Call:    substitute_hello_with_goodbye("Hello folks")
#   Returns: "Hello folks"
def substitute_hello_with_goodbye(string):
    if "hello" in string:
        return string.replace("hello", "goodbye")
    



# Purpose: removes the le_tter x from a string
# Example:
#   Call:    remove_x("xoxo")
#   Returns: "oo"
#   Call:    remove_x("OXO")
#   Returns: "OO"
def remove_x(string):
    if "x" in string:
        return string.replace('x','')
    elif "X" in string:
        return string.replace ('X','')
    else:
        return ''
    
    


# Purpose: returns the first half of a string
# Example:
#   Call:    first_half("coding")
#   Returns: "cod"
# Note: you can assume the string will always have an even number of characters
def first_half(string):
    return string[:len(string)//2]


# Purpose: returns the second half of a string
# Example:
#   Call:    second_half("coding")
#   Returns: "ing"
# Note: you can assume the string will always have an even number of characters
def second_half(string):
    return string[len(string)//2:]


# Congrats, you're done with this file. Move on to the next one.
