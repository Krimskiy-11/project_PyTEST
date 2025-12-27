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
