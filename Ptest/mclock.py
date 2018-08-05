import time, datetime
import math
import itertools
import tkinter
import threading

def get_clock_step(base_pntr, long_pntr):
    pos = []
    for i in range(60):
        pos.append((base_pntr[0]+long_pntr*math.cos(i*math.pi/30),
                    base_pntr[0]+long_pntr*math.sin(i*math.pi/30)))
    return pos[45:] + pos[:45]

def gen_i_pos(c_pntr, long_pntr):
    for i,p in enumerate(get_clock_step(c_pntr,long_pntr)):
        yield i,p

class Pointer:
    def __init__(self):
        pass