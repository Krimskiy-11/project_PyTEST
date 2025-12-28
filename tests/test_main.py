from src.easy_test import add_numbers, reverse_string, list_avg, needing_word
from tests.conftest import my_list
import pytest

@pytest.mark.parametrize('num1, num2, summa', [
    (2, 3, 5),
    (5, 5, 10),
    (20, 55, 75)
])
def test_easy_test(num1, num2, summa):
    assert add_numbers(num1, num2) == summa

@pytest.mark.parametrize("string, expected_result", [
    ("sasha", "ahsas"),
    ("suvorov", "vorovus"),
    ("cool", "looc"),
    ("", ""),
])
def test_reverse_string(string, expected_result):
    assert reverse_string(string) == expected_result


def test_list_avg(my_list):
    assert list_avg(my_list) == 3
    assert list_avg([]) == 0


@pytest.mark.parametrize('my_lst, my_type, result', [
    ([1, '23', [1, 2], 3, {}, (3, 28)], int, 2),
    ([1, '23', [1, 2], 3, {}, (3, 28)], str, 1),
    ([], list, 0),
    (['1, 23, [1, 2], 3, {}, (3, 28)'], dict, 0),
    ([1, '23', [1, 2], 3, {}, (3, 28), '12', '23HHH', 34], int, 3),
    (None, int, 0)
])
def test_needing_word(my_lst, my_type, result):
    assert needing_word(my_lst, my_type) == result

    # assert needing_word()