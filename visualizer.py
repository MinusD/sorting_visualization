import random
import time
import numpy as np
import os
import sys
import glob
from typing import Any
import cv2
from PIL import Image

import config as cfg


class Visualizer(list):
    def __init__(self) -> None:
        self.timer = time.time()
        self.counter = 0
        self.img_height: int
        self.img_width: int
        self.img = None
        self.pixels = None
        self.open_image()
        self.add_background()
        self.last_use = [[-1, (0, 0, 0)]] * (self.img_width * self.img_height)
        self.fill_list()
        super().__init__(self.last_use.copy())

        self.is_start = False
        self.out = cv2.VideoWriter(f'output_video_{round(time.time())}.avi', cv2.VideoWriter_fourcc(*'XVID'),
                                   cfg.FRAME_PER_SECOND, [self.img_width, self.img_height])
        debug(
            f'Приложение запущено\nШирина: {self.img_width}\nВысота: {self.img_height}\n'
            f'Пиксели: {self.img_width * self.img_height}')

    def start(self) -> None:
        self.is_start = True

    def add_background(self) -> None:
        """Добавляет вместо пустоты монотонный фон"""
        try:
            for i in range(self.img_width):
                for j in range(self.img_height):
                    r, g, b, a = self.pixels[i, j]
                    if a == 0:
                        self.img.putpixel((i, j), cfg.BACKGROUND_COLOUR)
        except Exception as e:
            debug('Заполнение фона не произошло')

    def open_image(self) -> None:
        """Открывает изображение и сохраняет размеры"""
        try:
            self.img = Image.open(cfg.IMG_FILENAME)
            self.pixels = self.img.load()
        except IOError:
            print("Не удалось открыть изображение")
            sys.exit(1)
        self.img_width, self.img_height = self.img.size

    def fill_list(self) -> None:
        """Заполняет список информацией о картинке"""
        for i in range(self.img_width * self.img_height):
            self.last_use[i] = [i, self.get_pixel(i)]
        debug('Сохраняем информацию о картинке')

    def get_pixel(self, i: int) -> list:
        """Возвращает список с цветом пикселя"""
        return [self.pixels[i % self.img_width, i // self.img_width]]

    def set_pixel(self, i, rgb) -> None:
        """Устанавливает цвет пикселя"""
        self.img.putpixel((i % self.img_width, i // self.img_width), rgb)

    def delay(self, seconds: int = 1) -> None:
        """Продлевает текущий кадр на указанное количество секунд"""
        for i in range(seconds * cfg.FRAME_PER_SECOND):
            img = np.array(self.img.copy().convert('RGB'))
            img = img[:, :, ::-1].copy()
            self.out.write(img)

    def __getitem__(self, item) -> Any:
        """Переопределение получения элемента по индексу"""
        return super().__getitem__(item)[0]

    def __setitem__(self, key, value) -> None:
        """Переопределение установки элемента по индексу"""
        for i in range(len(self.last_use)):
            if self.last_use[i][0] == value:
                super().__setitem__(key, [value, self.last_use[i][1]])
                self.set_pixel(key, tuple(self.last_use[i][1]))
                break

        if self.is_start:
            self.save_frame()

    def save_frame(self) -> None:
        """Сохраняет кадр"""
        if self.counter % cfg.TIMEOUT_FRAMES == 0:
            img = np.array(self.img.copy().convert('RGB'))
            img = img[:, :, ::-1].copy()
            self.out.write(img)
        self.counter += 1

    def save_video(self) -> None:
        """Сохранение видео"""
        self.out.release()
        debug(f'Выполнено за {round(time.time() - self.timer, 3)} с.')


def debug(data: Any):
    print(data)
