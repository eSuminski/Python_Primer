import re

phrase = "my mother loves me"
result = re.search("^my.*love", phrase)
# there are many ways to search through information, documentation is very helpful here
if result:
    print(type(result))
else:
    print("the criteria was not met")