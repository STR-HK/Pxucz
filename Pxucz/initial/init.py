from Pxucz.initial import set_variables
from Pxucz.utils import global_path
from OpenGL.GL import *
from OpenGL.GLU import *


def init(abspath: str):
    global_path.set_abs_path(path=abspath)
    set_variables.setvar()
