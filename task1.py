"""
__Бинарный поиск__


___Контекст___
Предположим, что мы хотим найти элемент в массиве (получить
его индекс). Мы можем это сделать просто перебрав все элементы.
Но что, если массив уже отсортирован? В этом случае можно
использовать бинарный поиск. Принцип прост: сначала берём
элемент находящийся посередине и сравниваем с тем, который мы
хотим найти. Если центральный элемент больше нашего,
рассматриваем массив слева от центрального, а если больше -
справа и повторяем так до тех пор, пока не найдем наш элемент.


___Ваша задача___
Написать программу на любом языке в любой парадигме для
бинарного поиска. На вход подаётся целочисленный массив и
число. На выходе - индекс элемента или -1, в случае если искомого
элемента нет в массиве.
"""

import random
from typing import List


def merge_sorting(numbers: List[int]) -> list:  # Метод сортировки слиянием
    """
    В целях соблюдения контекста, применяю метод сортировки слиянием для формирования отсортированного массива чисел.
    """

    if not isinstance(numbers, list):
        numbers = list(numbers)

    length = len(numbers)
    if length <= 1:
        return numbers

    middle = length // 2
    left_half = numbers[:middle]
    right_half = numbers[middle:]

    left_half = merge_sorting(left_half)
    right_half = merge_sorting(right_half)

    return connect_lists(left_half, right_half)


def connect_lists(left: list, right: list) -> list:  # Метод для соединения двух списков
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def binary_search(numbers, value, min_index, max_index):
    if max_index < min_index:
        return -1

    middle = (max_index - min_index) // 2 + min_index

    if numbers[middle] < value:
        return binary_search(numbers, value, middle + 1, max_index)

    if numbers[middle] > value:
        return binary_search(numbers, value, min_index, middle - 1)

    return middle


array_numbers = []  # Изначально пустой массив
for num in range(19):
    array_numbers.append(random.randint(1, 100))  # Генератор 19-ти случайных чисел в радиусе от 1 до 100
print(f"Массив случайных чисел перед сортировкой слиянием -> {array_numbers}")
print(f"Массив случайных чисел после сортировки слиянием -> {merge_sorting(array_numbers)}")
print(f"Индекс искомого элемента (50) -> {binary_search(merge_sorting(array_numbers), 50, 0, len(array_numbers) - 1)}")
