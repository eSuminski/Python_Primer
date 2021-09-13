import pytest
from begining_python.starter_python import MyClass

basic_class = MyClass(5, "our string")


def concatonate(word):
    result = word + "our new addition"
    return result


def addition(num):
    return num + 5


def test_basic():
    assert True
    # this is the basic format for a unit test
    # def test_name_of_test():
    #   whatever you are trying to test
    #   assert result you are looking for


def test_string_concatonation():
    word = "horse"
    assert concatonate(word) == "horseour new addition"


def test_add_five():
    number = 10
    assert addition(number) == 15


def test_MyClass_number():
    assert basic_class.number == 67
    # this test will fail because the basic_class number is actually 5
