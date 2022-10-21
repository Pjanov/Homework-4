# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

def get_non_repeating_elements(lst: list) -> list:
    new_lst = []
    for i in lst:
        if lst.count(i) == 1:
            new_lst.append(i)
    return new_lst

lst = [34, 34, 10, 45, 45, 39, 51, 51]

new_lst = get_non_repeating_elements(lst)
print('{} => {}'.format(lst, new_lst))
