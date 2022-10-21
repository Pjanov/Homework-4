# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# многочлена и записать в файл многочлен степени k.
# Коэффициенты должны быть случайными числами в диапазоне от 1 до 100
# Пример:
# - k=2 => 6*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0
# Усложнение: Коэффициенты в полиноме могут быть нулевыми.
# Примечание Создать три функции:
# 1) Функция формирования полинома. аргумент: степень полинома; возвращает полином.
# Коэффициенты вычисляются случайными.
# Полином удобно представить как словарь или как список коэффициентов. (на ваш выбор)
# В словаре степени будут ключами, в списке - индексами.
# Например k=3 => 6*x^3 + 4*x + 5. Словарь будет такой: {3:6, 2:0, 1:4, 0:5}. А список такой [5,4,0,6]
# 2) Функция формирование строки-полинома. Аргумент: полином (в вид словаря или списка).
# Возвращает строку вида '6*x^3 + 4*x + 5'
# Примечание: Обратите внимание на запись первой и нулевой степени, а также учет нулевого коэффициента.
# Для формирования строки удобно использовать join
# 3) Функция записи строки-полинома в файл. Аргументы: имя файла и строка-полином.


from random import randint


def create_coeffs(num: int) -> list:
    return [randint(1, 100) for _ in range(num + 1)]


def create_str(list_coeff: list) -> str:
    list_coeff = list_coeff[::-1]
    lst_str = []
    for idx, el in enumerate(list_coeff):
        lst_str.append(f'{el}*x^{len(list_coeff) - idx - 1}')
    my_str = ' + '.join(lst_str)
    my_str = my_str.replace('*x^0', ' = 0')
    my_str = my_str.replace('^1 +', ' +')
    return my_str


def write_to_file(polynom_string: str, filename: str) -> None:
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(polynom_string)


k = randint(2, 5)
list_coeff = create_coeffs(k)
str_pol = create_str(list_coeff)
print('{} => {}'.format(list_coeff, str_pol))

write_to_file(str_pol, 'Homework\Homework-4\Task_4.txt')
