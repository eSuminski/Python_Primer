basic_list = [1,2,3,4]

print(basic_list)

basic_list.append("I declare a thumb war") # this adds our string to the end of the list

print(basic_list)

list_to_extend = [5,6,7,8]

basic_list.extend(list_to_extend) # the values being added must be inside an iterable container

print(basic_list)

basic_list.insert(0,"Hey! Let's have a thumb war") # this adds the element before the indicated index position

print(basic_list)

basic_list.remove(7) # this removes the indicated object

print(basic_list)

print(basic_list.pop(3))
print(basic_list)

reverse_the_list = [1,2,3,4,5,6]
print(reverse_the_list)
reverse_the_list.reverse() # this method will reverse your list
print(reverse_the_list)
