import random
import time

from visualizer import Visualizer


def shuffle(vs: Visualizer):
    for x in range(len(vs)):
        i = random.randint(0, len(vs) - 1)
        j = random.randint(0, len(vs) - 1)
        data[i], data[j] = data[j], data[i]


if __name__ == '__main__':
    data = Visualizer()
    shuffle(data)
    data.delay()
    # Алгоритм сортировки тут, список заполнять не нужно
    for i in range(len(data)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(data)):
            if data[j] < data[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        data[i], data[lowest_value_index] = data[lowest_value_index], data[i]

    # for i in range(len(data)):
    #     for j in range(len(data) - i - 1):
    #         if data[j] > data[j + 1]:
    #             data[j], data[j + 1] = data[j + 1], data[j]

    data.save_video()
