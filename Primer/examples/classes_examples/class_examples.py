from abc import ABC, abstractmethod


class MyNewClass:
    def __init__(self, age=0, name="default name"):
        self.name = name
        self.age = age

    def my_new_class_function(jeeves):  # first parameter is always a reference to self, doesn't have to be called self
        return "this is my class function"

    def __str__(jeeves):
        return f"my name is {jeeves.name} and my age is {jeeves.age}"

    def __repr__(self):
        return f"MyNewClass(self,{self.age},{self.name})"


# my_class = MyNewClass()
#
# print(my_class.__str__())
# # print(MyNewClass.__str__(my_class)) this is the same as the above

class MyAbstractClass(ABC):
    class_count = 0

    @classmethod
    def print_class_count(cls):
        return cls.class_count

    @abstractmethod
    def to_be_determined(self):
        pass


class MyInheritsTheAbstractClass(MyAbstractClass):

    def __init__(self):
        print("I inherited from the abstract class")
        MyAbstractClass.class_count = MyAbstractClass.class_count + 1

    def to_be_determined(self):
        return "I have defined what this function actually does"


class AlsoInheritsAbstractmethod(MyAbstractClass):
    def __init__(self):
        print("I also inherited from the abstract class")
        MyAbstractClass.class_count = MyAbstractClass.class_count + 1

    def to_be_determined(self):
        return "I have also defined what this function does"


# my_class = MyInheritsTheAbstractClass()
# print(my_class.print_class_count())
# my_other_class = AlsoInheritsAbstractmethod()
# print(my_other_class.print_class_count())
# print(my_class.to_be_determined())
# print(my_other_class.to_be_determined())

class OuterClass:
    def __init__(self, number, word, inner_class="my inner class"):
        self.number = number
        self.word = word
        self.create_inner_class(inner_class)

    class InnerClass:
        def __init__(self, name):
            self.name = name
            print("the inner class has been created")

    def create_inner_class(self, name):
        self.inner_class = self.InnerClass(name)

    def __str__(self):
        return f"my number is {self.number}, my word is {self.word}, and my inner class is called {self.inner_class.name}"


# outter_class = OuterClass(5, "pie")
# print(str(outter_class))

class InheritedConstructor:
    def __init__(self, name):
        self.name = name
        print("the parent constructor was called")


class Inheritsconstructor(InheritedConstructor):
    def __init__(self, age, name):
        # super(Inheritsconstructor, self).__init__(name)
        super().__init__(name)
        self.age = age
        print("the child class constructor was called")

class A:
    def __init__(self):
        print("parent constructor was called")

class B(A):
    def __init__(self):
        super(B, self).__init__()
        print("the child was called")

class StaticMethodsClass:
    def __init__(self):
        print("my class was instantiated")

    @staticmethod
    def print_a_phrase():
        return "This has nothing to do with any instantiated objects from this class"

print(StaticMethodsClass.print_a_phrase())

