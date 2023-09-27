# == INSTRUCTIONS ==
#
# Purpose: Validate a password
# Parameters: one, a string
# Rules:
#   - It must be longer than 7 characters (8 is fine)
#   - It must contain at least one of the following special characters: `!`, `@`,
#     `$`, `%` or `&`
# Returns: a boolean (True if valid, False otherwise)
# Example:
#   Call:    is_valid("1234567")
#   Returns: False
#   Call:    is_valid("12345678")
#   Returns: False
#   Call:    is_valid("12345!78")
#   Returns: True

# == YOUR CODE ==

def is_valid(password):
    # setting current status of password is to False
    status = False
    # checking length of characters 
    if len(password) >=8:
    
    #checking for special characters 
        special_characters = ['!','@','$','%','&']

        for char in password:
            if char in special_characters:
                #change status to True if this condition is met
                status = True
    return status
    

