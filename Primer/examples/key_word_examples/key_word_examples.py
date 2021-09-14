from to_import import MyClass as z
# from indicates where the code is coming from
# import tells you what code is actually being brought into the module
# as sets a reference to the code you are importing

my_list = ["eric", "suminski"]
for name in my_list:
    print(name)

# for is used to create a loop, and in is used when you want to access elements within a list or other collection

x = 0
while x < 5:
    print(x)
    x =  x + 1

long_word = "thdufoewnd;wndd;"
for number in range(len(long_word)):
    print(number)


my_class = z("my imported class")

print(my_class.say_my_name())

name_one = "Eric"
name_two = "Sam"

if name_one is name_two:
    print("these are the same")
elif name_one is not name_two:
    print("these are not the same")
else:
    print("these are not the same")

if name_one is name_two:
    print("these are the same")
elif name_one is name_two and len(name_one) <= 10:
    print("the second condition was met")
else:
    print("these are not the same")
