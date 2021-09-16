my_text = open("file_handling/my_text.txt")
print(my_text.read())
my_text.close()
# make sure you close your file after you are done with it

my_text_to_append = open("file_handling/my_text.txt", "a")
my_text_to_append.write(" I added this text via my Python program")
my_text_to_append.close()

my_text = open("file_handling/my_text.txt")
print(my_text.read())
my_text.close()

overwrite_text = open("file_handling/my_text.txt", "w")
overwrite_text.write("I believe this overwrites the current text")
overwrite_text.close()

overwrite_text = open("file_handling/my_text.txt")
print(overwrite_text.read())
overwrite_text.close()

# if you use the with keyword you do not need to worry about closing the file: Python will do it for you
with open("file_handling/my_text.txt", "w") as file:
    file.write("I don't need to close this file")

with open("file_handling/my_text.txt") as to_read:
    print(to_read.read())