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
        self.img_height: int
        self.img_width: int
        self.img = None
        self.pixels = None
        self.open_image()
        self.add_background()
        super().__init__([-1] * (self.img_width * self.img_width))
        self.fill_list()
        self.counter = 0
        self.is_start = False

        debug('Приложение запущено')

    def add_background(self):
        """Добавляет вместо пустоты монотонный фон"""
        for i in range(self.img_width):
            for j in range(self.img_height):
                r, g, b, a = self.pixels[i, j]
                if a == 0:
                    self.img.putpixel((i, j), cfg.BACKGROUND_COLOR)
        # self.img.show()

    def open_image(self):
        try:
            self.img = Image.open('img.png')
            self.pixels = self.img.load()
        except IOError:
            print("Не удалось открыть изображение")
            sys.exit(1)
        self.img_width, self.img_height = self.img.size
        print(self.img_width, self.img_height)

    def fill_list(self):
        for i in range(self.img_width * self.img_height):
            super().__setitem__(i, i)

    def get_counter(self):
        return '{:0<5}'.format(str(self.counter))

    def __getitem__(self, item):
        if self.is_start:
            self.save_frame()
        return super().__getitem__(item)

    def save_frame(self):
        pass


def debug(data: Any):
    print(data)
