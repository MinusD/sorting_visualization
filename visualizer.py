import random
import os
import sys
import glob
from typing import Any

import tkinter.ttk as ttk
from tkinter import *
from PIL import Image


class Visualizer:
    def __init__(self):
        self.app_path = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.get_images()
        debug('Приложение запущено')

    def get_images(self) -> list:
        for address, dirs, files in os.walk(self.app_path):
            print(address, dirs, files)


def debug(data: Any):
    print(data)
