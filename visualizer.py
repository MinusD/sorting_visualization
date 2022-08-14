import random
import os
import sys
import glob
from typing import Any

import tkinter.ttk as ttk
from tkinter import *
from PIL import Image

import config as cfg


class Visualizer(list):
    def __init__(self):
        self.path = None
        self.img_height: int
        self.img_width: int
        self.img = None
        self.pixels = None
        self.open_image()
        self.add_background()
        super().__init__([[-1, (0, 0, 0, 0)]] * (self.img_width * self.img_height))
        self.last_use = [[-1, (0, 0, 0, 0)]] * (self.img_width * self.img_height)
        self.fill_list()

        self.create_tmp_dir()
        self.counter = 0
        self.is_start = True

        debug(
            f'Приложение запущено\nШирина: {self.img_width}\nВысота: {self.img_height}\n'
            f'Пиксели: {self.img_width * self.img_height} - {super().__len__()}')

    def create_tmp_dir(self) -> None:
        """Создаёт временную директорию"""
        app_path = os.path.dirname(os.path.realpath(sys.argv[0]))  # Папка, откуда запускаемся
        self.path = os.path.join(app_path, 'tmp')
        os.makedirs(self.path, exist_ok=True)

    def add_background(self):
        """Добавляет вместо пустоты монотонный фон"""
        for i in range(self.img_width):
            for j in range(self.img_height):
                r, g, b, a = self.pixels[i, j]
                if a == 0:
                    self.img.putpixel((i, j), cfg.BACKGROUND_COLOR)

    def open_image(self):
        """Открывает изображение и сохраняет размеры"""
        try:
            self.img = Image.open('img2.png')
            self.pixels = self.img.load()
        except IOError:
            print("Не удалось открыть изображение")
            sys.exit(1)
        self.img_width, self.img_height = self.img.size

    def fill_list(self):
        """Заполняет список информацией о картинке"""
        for i in range(self.img_width * self.img_height):
            super().__setitem__(i, (i, self.get_pixel(i)))
            self.last_use[i] = [i, self.get_pixel(i)]

    def get_pixel(self, i: int) -> list:
        """Массив с цветом пикселя"""
        return [self.pixels[i // self.img_height, i % self.img_height]]

    def set_pixel(self, i, rgb) -> None:
        """Устанавливает цвет пикселя"""
        self.img.putpixel((i // self.img_height, i % self.img_height), rgb)

    def get_counter(self):
        """Счётчик с незначащими нулями"""
        return '{:0>5}'.format(str(self.counter))

    def __getitem__(self, item):
        if self.is_start:
            pass
            # self.save_frame()

        # print(super().__getitem__(item))
        return super().__getitem__(item)[0]

    def __setitem__(self, key, value):
        for i in range(len(self.last_use)):
            if self.last_use[i][0] == value:
                super().__setitem__(key, [value, self.last_use[i][1]])
                self.set_pixel(key, tuple(self.last_use[i][1]))
                break

        # self.set_pixel(key, 123)
        if self.is_start:
            # pass
            self.save_frame()

    def save_frame(self):
        """Сохраняет кадр"""
        self.img.save(f'tmp\\frame-{self.get_counter()}.png')
        self.counter += 1


def debug(data: Any):
    print(data)
