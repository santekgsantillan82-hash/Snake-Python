import os
import sys

def recurso(ruta):
    if hasattr(sys, "_MEIPASS"):
        base = sys._MEIPASS
    else:
        base = os.path.abspath(".")

    return os.path.join(base, ruta)