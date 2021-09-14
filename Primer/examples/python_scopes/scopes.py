name = "Eric Suminski"  # this is globally accessible


def outer_function():
    name = "Sam Suminski"
    # return name
    return inner_function()


def inner_function():
    global name
    name = "new name"
    return name

outer_function()
print(name)
