"""This is a docstring: you use triple double quotes to create them"""

# it is very easy to create a variable in python

my_variable = "you give it a name and a value"

my_number = 10

my_second_number = 10.1

my_boolean = True

my_empty_void = None


# it is also very easy to create functions

def my_function(result: str) -> str:
    """this is the docstring for my function. It should explain what the function does"""
    result = result + "I added this string value"
    return result


# functions do not have to return anything
def does_not_return_anything():
    print("technically not returning anything")


# this has a default value
def this_has_default_params(result="default"):
    print(result)


# Python does have lambdas
# this example concatanates strings
# common way to use lambdas is to put them in other functions

# name = "eric"
#
# (lambda x: print(name))(name)

def concatonate(word):
    return lambda c: c + " " + word


new_name = concatonate("suminski")

print(new_name("Eric"))


def add(number: int):
    return lambda a: a + number


new_number = add(5)

print(new_number(6))  # this will return 11

new_number = add(100)

print(new_number(6))  # this will return 106


# classes are also simple to create
class NestedClass:
    def __init__(self, my_string = "this is cool"):
        self.my_string = my_string


class MyClass:
    class_variable = "this is available to all instances"
    inheritance_note = "if you want to inherit from another class then add them to the parameters"
    __private_class = NestedClass()

    def __init__(self, number, a_string="this is a default string"):
        self.number = number
        self.a_string = a_string
        # notice the instance variables are defined in the constructor
        # you can only have your one constructor
        # default arguments must go at the end of the parameters




class ChildClass(MyClass):

    def __init__(self, number):
        super().__init__(number)
        # the child class can call the parent class's constructor and use it


# a simple statement is one line of code

simple_statement = "this is a single line of code"

# a compound statement involves more than one line of code. When using compound statements be sure to get
# your indentation correct.

if simple_statement == "this is a single line of code":
    print("I can spell") # this line needs to be indented
else:
    print("I can't spell") # this line needs to be indented