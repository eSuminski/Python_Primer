import pytest

from custom_exceptions.my_exception import MyException


def trigger_exception(num):
    if num == 0:
        return True
    else:
        raise MyException("this is the custom message I give this exception")


def test_first_run():
    result = trigger_exception(0)
    assert result


# def test_second_run():
#     assert trigger_exception(1)
# this shows us the exception is working, but the test fails...

def test_third_run():
    with pytest.raises(MyException):
        result = trigger_exception(1)
        assert result


def test_fourth_run():
    with pytest.raises(MyException):
        result = trigger_exception(0)
        assert result
        # this test will fail despite result = True because the test is expecting an exception called MyException
