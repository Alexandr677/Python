# Напишите программу, которой на вход подается последовательность чисел через пробел, а также запрашивается
# у пользователя любое число.
# В качестве задания повышенного уровня сложности можете выполнить проверку соответствия указанному в условии
# ввода данных.
# Далее программа работает по следующему алгоритму:
# Преобразование введённой последовательности в список
# Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
# Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше
# или равен этому числу.
# При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен в этом модуле.
# Реализуйте его также отдельной функцией.
def sortins(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx-1] > x:
          array[idx] = array[idx-1]
          idx -= 1
        array[idx] = x
    return array
def binary_search(array, element, left, right):
    middle = (right + left) // 2  # находимо середину
    if left > right or element >= max(array):  # если левая граница превысила правую, или элемент больше или равен
        # максимальному значению в массиве
        return False  # значит элемент отсутствует


    if array[middle] < element and array[middle+1] >= element:  # если элемент соответствует условию задачи то,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)
def typetrue(str):
    str_norm = ['0','1','2','3','4','5','6','7','8','9',' ']
    typetr = True
    for i in range(len(str)):
        if str[i] not in str_norm:
            # print(f'{i+1} введеный символ НЕ соответствует условиям')
            typetr = False
    return typetr

while True:
    str = input('Введите последовательность чисел через пробел')
    str_element = input('Введите число для которого будет искаться индекс в массиве в соответствии с условиями')
    if typetrue(str) and typetrue(str_element):
        break
    else:
        print('Вы ввели неправильные данные. Попробуйте еще раз')
element = int(str_element)
array = list(map(int, str.split()))
print(f'Массив: {array}')
array_sort = sortins(array)
print(f'Массив после сортировки: {array_sort}')
print(f'Индекс элемента: {binary_search(array, element, 0, len(array_sort))}')