# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Написать функцию, которая принимает аргумент - целое число и возвращает список его простых множителей.
# Пример:
# simple_number(147420) => [2, 3, 5, 7, 13];
# simple_number(374220) => [2, 3, 5, 7, 11];

def list_of_multipliers(val):
    my_list = []
    n = 2
    while val >= n:
        if val % n == 0:
            my_list.append(n)
            val /= n
        else:
            n += 1
    return set(my_list)


simple_number = 1474200
print(f'simple_number({simple_number}) =>', list(list_of_multipliers(simple_number)))
