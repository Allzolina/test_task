# Поиск суммы всех четных чисел
numbers = [2, 5, 88, 99, 21, 56, 43, 5, 88, 13, 23, 21]


def sum_even_number(numbers):
    sum = 0
    for number in numbers:
        if number % 2 == 0:
            sum += number
    return sum


print(sum_even_number(numbers))

# Поиск всех комбинаций трех листов
list1 = [1, 3, 4]
list2 = [6, 7, 9]
list3 = [8, 10, 5]


def calculate_combination_list(list1, list2, list3):
    combination_list = []
    for number_list1 in list1:
        for number_list2 in list2:
            for number_list3 in list3:
                combination = [number_list1, number_list2, number_list3]
                combination_list.append(combination)
    return combination_list


print(calculate_combination_list(list1, list2, list3))
