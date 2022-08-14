import random

from visualizer import Visualizer


def shuffle(vs: Visualizer):
    for x in range(len(vs)):
        i = random.randint(0, len(vs) - 1)
        j = random.randint(0, len(vs) - 1)
        tmp = vs[i]
        vs[i] = vs[j]
        vs[j] = tmp


if __name__ == '__main__':
    data = Visualizer()
    shuffle(data)
    # Алгоритм сортировки тут, список заполнять не нужно
    print(len(data))
    for i in range(len(data)):
        print(data[i])
    # print(data[100])
    # for i in range(len(data)):
    #     for j in range(len(data) - i - 1):
    #         if data[j] > data[j + 1]:
    #             data[j], data[j + 1] = data[j + 1], data[j]
