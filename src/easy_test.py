def add_numbers(num1, num2):
    """Функция, складывающая два числа"""
    return num1 + num2

def is_even(num):
    """Функция, проверяющая, является ли число четным"""
    if num % 2 == 0:
        return True
    else:
        return False

def find_max(numbers):
    """Функция, находящая максимальное значение из списка чисел"""
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def say_this(word):
    return word

def reverse_list(lst):
    return lst[::-1]

def reverse_string(word):
    return word[::-1]


def list_avg(lst):
    if len(lst) > 0:
        return sum(lst) / len(lst)
    return 0

def needing_word(lst, my_type):
    result = 0
    if isinstance(lst, list):
        for i in lst:
            if isinstance(i, my_type):
                result += 1
    return result