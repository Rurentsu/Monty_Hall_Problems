
from src.myclass import Strategy
import numpy as np
from math import sqrt, pi, exp
from random import randint, seed
from matplotlib import pyplot as plt

def play_game(strategy):
    doors = [0, 1, 2]
    right_door = randint(0, 2)
    first_choice = randint(0, 2)
    doors.remove(first_choice)

    if first_choice == right_door:
        doors.remove(doors[randint(0, 1)])
    else:
        doors = [right_door]
    second_choice = 0

    if strategy == Strategy.CHANGE:
        second_choice = doors[0]
    elif strategy == Strategy.STAY:
        second_choice = first_choice
    else:
        print("Unknow strategy!")
    
    return second_choice == right_door