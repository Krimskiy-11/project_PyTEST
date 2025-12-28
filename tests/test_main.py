from src.easy_test import add_numbers, is_even, find_max, say_this, reverse_list
from tests.conftest import my_list


def test_easy_test(my_list):
    # assert add_numbers(numbers, numbers) == 4

    assert is_even(4)
    assert is_even(3) == False

    # assert say_this(numbers) == 'hi'

    assert find_max(my_list) == 5

    assert reverse_list(my_list) == [5, 4, 3, 2, 1]