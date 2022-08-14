import random
import os
import sys
import glob
import re
from typing import Any

import tkinter.ttk as ttk
from tkinter import *
from PIL import Image

PADDING = 20


class Visualizer:
    def __init__(self):
        self.img_height = None
        self.img_width = None
        self.img = None
        self.app_path = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.window = Tk()
        self.window.title('Настройки')
        self.window.geometry('185x200')

        self.img_combo = ttk.Combobox(self.window, state="readonly")
        self.img_combo['values'] = self.get_images()
        self.img_combo.current(0)
        self.img_combo.grid(column=1, row=2, padx=PADDING, pady=PADDING)

        self.btn_set_img = Button(self.window, text="Далее", command=self.open_image)
        self.btn_set_img.grid(column=1, row=3, padx=PADDING, pady=PADDING)

        self.window.mainloop()
        debug('Приложение запущено')

    def get_images(self) -> list:
        """Список картинок png или jpg"""
        filenames = glob.glob(os.path.join(self.app_path, "*.png"))
        filenames += glob.glob(os.path.join(self.app_path, "*.jpg"))
        filenames = [re.search(r'.*\\(.+\.(png|jpg))', filename).group(1) for filename in filenames]
        return filenames

    def open_image(self):
        try:
            self.img = Image.open(self.img_combo.get())
        except IOError:
            print("Не удалось открыть изображение")
            sys.exit(1)
        self.img_width, self.img_height = self.img.size
        print(self.img_width, self.img_height)

    def go(self) -> None:
        pass


class SortingList(list):
    def __init__(self):
        self.vz = Visualizer()


def debug(data: Any):
    print(data)


if __name__ == '__main__':
    SortingList()
