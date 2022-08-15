import random
import time
import math

from visualizer import Visualizer


def shuffle(vs: Visualizer):
    for x in range(len(vs)):
        i = random.randint(0, len(vs) - 1)
        j = random.randint(0, len(vs) - 1)
        data[i], data[j] = data[j], data[i]


if __name__ == '__main__':
    data = Visualizer()
    data.start()
    shuffle(data)
    data.delay()

    # /* Сортировка пузырьком (Очень долгая, даже на маленькой картинке)
    '''
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    '''
    # Сортировка пузырьком */

    # /* Сортировка вставками
    # '''
    for i in range(len(data)):
        lowest_value_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[lowest_value_index]:
                lowest_value_index = j
        data[i], data[lowest_value_index] = data[lowest_value_index], data[i]
    # '''
    # Сортировка вставками */

    # /* Сортировка Шелла
    '''
    n = len(data)
    k = int(math.log2(n))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = data[i]
            j = i
            while j >= interval and data[j - interval] > temp:
                data[j] = data[j - interval]
                j -= interval
            data[j] = temp
        k -= 1
        interval = 2 ** k - 1
    '''
    # Сортировка Шелла */

    data.save_video()
