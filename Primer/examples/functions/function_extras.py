
def basic_function():
    return "this is the basic function"

def basic_function_2(parameter):
    return parameter + 1 # you can add an argument to this function and get it back plus 1

def add_type_annotation(param1: str, param2: int) -> str:
    return "you are indicating you want a string and int param entered into this function and you expect a string back"

def annotations_dont_matter(num: int, num2: int) -> int:
    return num + num2

print(annotations_dont_matter(3,5)) # this works as expected
print(annotations_dont_matter("these"," are not numbers")) # this also works, despite types not matching annotation

def variable_arguments(*args): # use this vararg when you don't know how much information the function will work with
    for element in args:
        print(element)
variable_arguments(1,2,3,4,5)

def vararg_many_objects(*can_be_named_whatever): # the convention is to call it args, but you can name it what you want
    for element in can_be_named_whatever:
        print(element)

vararg_many_objects(1,"two",3,"four")

def key_word_function(**kwargs): # this adds key:value arguments into your function
    print(kwargs["password"])
    print(kwargs["username"])

key_word_function(password="my password", username="my username")

def more_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

more_kwargs(first_key="first value", second_key="second value", third_key="third_value")

def calls_a_function(function):
    return function()

def called_function():
    return"this is called by the first function"

print(calls_a_function(called_function)) # leave off the parentheses: you want the reference for the method, not to call it