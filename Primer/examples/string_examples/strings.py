"""this is my docstring that gives info about the module"""

my_other_string = 'I made this with single quotes'
my_string = "this is a string"
my_other_other_string = """this is also a string"""
# you can create a string by using single, double, or triple double quotes

multi_line_string = """this should also work
if I give it extra spacing
it should work as a multiline string"""
# each new line is its own new line when printed
print(multi_line_string)

my_name = "Eric" # the actual string itself is the string literal
another_reference = "Eric"
a_third_reference = "Eric"
# Python sometimes uses string interning. It is where references to the same string are considered the same object
# String interning sometimes is used, it depends on the interpreter
print(id(my_name))
print(id(another_reference))
print(id(a_third_reference))

incomplete_name = 'Eric {last_name}'
print(incomplete_name)
print(incomplete_name.format(last_name= 'Suminski'))

first_name = "Sam"
last_name = "Suminski"
full_name = f"{first_name} {last_name}"
print(full_name)
print(full_name[0])

for character in full_name:
    print(character)

# when iterating through a string you can determine the start, stop, and increment values
# [start position: stop position: increment value]
# using the [] is string slicing
for character in full_name[::-1]: # this here is the exception, it will start at the back and work to the front
    print(character)

for character in full_name[3:6:1]:
    print(character)

for character in full_name[::2]:
    print(character)

for character in full_name[:8:]:
    print(character)

for character in full_name[::-2]:
    print(character)
