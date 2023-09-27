# == INSTRUCTIONS ==
#
# In these exercises you will define your own functions.
#
# Most functions will take a list or a dictionary as an argument, but some will
# take other arguments and some won't take any.
#
# The requirements will always start with the name of the function. Use this
# name exactly or the tests won't be able to find it.
#
# Then there will be a description of what the function should do. Note that
# some solutions will require more than one line of code.
#
# You won't find everything that you need in our materials. Use the Python Docs
# and Google liberally if you get stuck.

# == LIST EXERCISES ==

# Method name: first_element
# Purpose: returns the first element of the given list
# Arguments: one list
# Example:
#   Call:    first_element([1, 2, 3])
#   Returns: 1


def first_element(list):
    return list[0]
    


# Method name: second_element
# Purpose: returns the second element of the given list
# Arguments: one list
# Example:
#   Call:    second_element([1, 2, 3])
#   Returns: 2


def second_element(list):
    return list[1]

# Method name: last_element
# Purpose: returns the last element of the given list
# Arguments: one list
# Example:
#   Call:    last_element([1, 2, 3])
#   Returns: 3

def last_element(list):
    return list[-1]
    
# Method name: first_two_elements
# Purpose: returns the first two elements of the given list
# Arguments: one list
# Example:
#   Call:    first_two_elements([1, 2, 3])
#   Returns: [1, 2]
def first_two_elements(list):
    return list[0:2]


# Method name: first_three_elements
# Purpose: returns the first three elements of the given list
# Arguments: one list
# Example:
#   Call:    first_three_elements([1, 2, 3, 4])
#   Returns: [1, 2, 3]

def first_three_elements(list):
    return list[0:3]

    

# Method name: total
# Purpose: returns the sum of all the elements in the given list
# Arguments: one list
# Example:
#   Call:    total([1, 2, 3])
#   Returns: 6

def total(list):
    sum_of_list = sum(list)
    return sum_of_list 


# Method name: lowest_number
# Purpose: returns the lowest number in the given list
# Arguments: one list
# Example:
#   Call:    lowest_number([4, 2, 6])
#   Returns: 2
def lowest_number(list):
    list_in_ascending_order = sorted(list)
    lowest_number = list_in_ascending_order[0]
    return(lowest_number)



# Method name: highest_number
# Purpose: returns the highest number in the given list
# Arguments: one list
# Example:
#   Call:    highest_number([4, 6, 2])
#   Returns: 6

def highest_number(list):
    #sort th list from lowest number to highest number 
    list_in_ascending_order2 = sorted(list)
    #take this sorted list and return the highest number(last number/element)since it is in ascending order
    highest_number =list_in_ascending_order2[-1]
    return highest_number 

# Method name: the_beatles
# Purpose: returns the list ['john', 'paul', 'george', 'ringo']
# Arguments: none
# Example:
#   Call:    the_beatles()
#   Returns: ['john', 'paul', 'george', 'ringo']
def the_beatles(): 
    the_beatles_names = ["john", "paul", "george", "ringo"]
    return the_beatles_names


# Method name: i_joined_the_beatles
# Purpose: adds the given name to the list ['john', 'paul', 'george', 'ringo']
# Arguments: one string
# Example:
#   Call:    i_joined_the_beatles('yoko')
#   Returns: ['john', 'paul', 'george', 'ringo', 'yoko']
def i_joined_the_beatles(new_name):
    the_beatles_names_updated = ["john", "paul", "george", "ringo"]
    # add the inputed (new_name) to the original beatles list
    #add a new element to a list
    the_beatles_names_updated.append(new_name)
    return the_beatles_names_updated


# Method name: we_joined_the_beatles
# Purpose: adds the given names to the list ['john', 'paul', 'george', 'ringo']
# Arguments: one list
# Example:
#   Call:    we_joined_the_beatles(['yoko', 'stuart'])
#   Returns: ['john', 'paul', 'george', 'ringo', 'yoko', 'stuart']

def we_joined_the_beatles(list_of_names):
    #we have a list of names which is:
    beatles_names =['john', 'paul', 'george', 'ringo']
# we want to take the new list of names inside of our argument/our input and add them to our current list above
    beatles_names.extend(list_of_names)
    return beatles_names




# Method name: remove_nones_from_list
# Purpose: removes all the None values from the given list
# Arguments: one list
# Example:
#   Call:    remove_nones_from_list([1, None, 2, None, 3])
#   Returns: [1, 2, 3]

def remove_nones_from_list(lists):
#creating an empty list to store all of the list items without none values
    new_list_non_none_values = []
#look at every itemin the given list 
    for item  in lists:
#if the item in the given list is not None
        if item != None:#filtering condition
# take this item and add it to our new list
            new_list_non_none_values.append(item)
    return new_list_non_none_values


# Method name: double_list
# Purpose: returns a list with all the elements of the given list repeated twice
# Arguments: one list
# Example:
#   Call:    double_list([1, 2, 3])
#   Returns: [1, 2, 3, 1, 2, 3]

def double_list(list):
    new_list = list * 2
    return new_list 

# Method name: unique_elements
# Purpose: returns a list with all the unique elements of the given list
# Arguments: one list
# Example:
#   Call:    unique_elements([1, 2, 1, 3, 2, 3])
#   Returns: [1, 2, 3]

def unique_elements(list):
    unique_list_elements = []
    for items in list:
        if items in unique_list_elements:
            continue
        else:
            unique_list_elements.append(items) 
    return unique_list_elements

# Method name: add_to_list
# Purpose: adds the given element to the given list
# Arguments: one list and one element
# Example:
#   Call:    add_to_list(["a", "b", "c"], "d")
#   Returns: ["a", "b", "c", "d"]

def add_to_list(list, element):
    appended_list = list
    element_list = element
    appended_list.append(element_list)

    return appended_list


# == DICTIONARY EXERCISES ==

# Method name: new_band_member
# Purpose: merges a given dictionary into an existing dictionary
# Arguments: one dictionary
# Note: {"vocalist": "miss piggy", "lead_guitar": "scooter"}
# Example:
#   Call:    new_band_member({"bass": "flea"})
#   Returns: {"vocalist": "miss piggy", "lead_guitar": "scooter", "bass": "flea"}


def new_band_member(new_members): # function which stores new dictionary
    band_members = {"vocalist": "miss piggy", "lead_guitar": "scooter"}
    band_members.update(new_members)
    return band_members
    


# Method name: all_values
# Purpose: returns a list of all the values in the given dictionary
# Arguments: one dictionary
# Example:
#   Call:    all_values({"a": 1, "b": 2, "c": 3})
#   Returns: [1, 2, 3]
def all_values(dict):
    #take all the values from the given dictionary using the value function and chaging this into a list type and returning the values in a list
    all_values = list(dict.values())
    return all_values




# Method name: all_keys
# Purpose: returns a list of all the keys in the given dictionary
# Arguments: one dictionary
# Example:
#   Call:    all_keys({"a": 1, "b": 2, "c": 3})
#   Returns: ["a", "b", "c"]

def all_keys(dict):
    #take all the values from the given dictionary using the value function and chaging this into a list type and returning the values in a list
    all_keys = list(dict.keys())
    return all_keys

# Method name: remove_nones_from_dictionary
# Purpose: removes all pairs from a given dictionary where the value is None
# Arguments: one dictionary
# Example:
#   Call:    remove_nones_from_dictionary({"a": 1, "b": None, "c": 3})
#   Returns: {"a": 1, "c": 3}

#Pseduocode:
# #function needs to loop through all values of my_dict
# if value == None:
#     remove current key value pair from my_dict

#return mydict
#loop through all keys and values in dict
#if value is equal to None remove both key and value 


"""
Pseudocode
Go through every single key : value pair in the dictionary
if key has a value of None:
    we need to remove that key : value pair from the dictionary
return dictionary
"""
def remove_nones_from_dictionary(my_dict):
    for key, value in my_dict.items():
        if value == None:
            none_values = my_dict.pop(key,value)
            return my_dict


# Method name: touch_in
# Purpose: creates a dictionary from a given tube station and time
# Arguments: two strings, one for the tube station and one for the time
# Example:
#   Call:    touch_in('Aldgate East', '2022/01/30 17:12')
#   Returns: {'entrypoint': 'Aldgate East', 'time': '2022/01/30 17:12'}

#pseudocode
# define a function called touch_in() which takes two arguments
#called (tube_station, time)
#declare empty dictionary called underground_tap_in
#inside underground_tap_in 
#key value pairs to add {'entrypoint': tube_station, 'time': time}
#return underground_tap_in

def touch_in(tube_station, time):
    underground_tap_in = {

    'entrypoint': tube_station,
    'time': time 

    }
    return underground_tap_in 















#convert two strings into a dictionary
# returns the sting one and string 2  
# def touch_in(string1, string2):
#     #create a new empty empty dictionary to store the tube names and tube stations

#     pass