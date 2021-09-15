def key_function():
    return "this is showing how functions work in keys"

my_dictionary = { # you can mix and match keys and values as you need
    "key":"value",
    "can also have number values": 10,
    1:"my key is the number 1",
    2:3,
    "None is a valid value": None,
    None: "this is also valid",
    key_function(): "this is also a valid setup", # this key is actually calling the function
    "this is the key for the function": key_function # this is a reference to the function
}

print(my_dictionary)

my_dictionary["this is my new key"] = "the new value" # this adds a new key value pair to the dictionary

print(my_dictionary)

print(my_dictionary.items()) # returns the key value pairs as tuples

