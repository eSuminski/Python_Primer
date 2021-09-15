# these are not indexable, but they are iterable
my_set = {"eric","sam"}

print(my_set)

my_set.add("luke")

print(my_set)

other_siblings = {"jed", "katie", "kristen"}


my_set.update(other_siblings)
print(my_set)
