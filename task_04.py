# Написать функцию, возвращающую количество комбинаций заданного набора весов грузиков для заданного веса.
# Результат приложить в виде ссылки на fiddle удобного языка (типа http://pythonfiddle.com/)
# Примечание: в комбинации не должно присутствовать два или более одинаковых грузиков,
# но можно задать в изначальном наборе несколько одинаковых грузиков и в таком случае их все можно использовать
# для формировыания комбинации.


import numpy as np


def to2(n, len_list):
    array = np.zeros(len_list, dtype=np.int8)
    i = len_list - 1
    while n > 0:
        array[i] = n % 2
        n //= 2
        i -= 1
    return array


cargo_weight = int(input('Введите вес заданного груза в граммах:\n'))
weights = input('Введите через пробел набор весов грузиков в граммах.\nНапример:\n1 5 5 10\n')
list_weights = np.array(sorted(tuple(map(int, weights.split(' ')))))
len_list_weights = len(list_weights)
count = 0

for i in range(0, 2 ** len_list_weights):
    r = list_weights * to2(i, len_list_weights)
    if sum(r) == cargo_weight:
        count += 1

print('Количество комбинаций: ', count)
