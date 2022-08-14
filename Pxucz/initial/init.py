import time

from Pxucz.initial import set_variables
from Pxucz.utils import global_path
from OpenGL.GL import *
from OpenGL.GLU import *
from Pxucz.initial import opener as px_opener
import threading


def init(abspath: str, loader_size_x: int, loader_size_y: int):
    global_path.set_abs_path(path=abspath)
    set_variables.setvar()
    loaderThread = threading.Thread(target=px_opener.start, args=(loader_size_x, loader_size_y))
    loaderThread.start()
