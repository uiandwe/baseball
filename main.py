# -*- coding: utf-8 -*-
from number.RandomBaseballNumber import RandomBaseballNumber
from controller.BaseballGame import BaseballGame

if __name__ == '__main__':
    random_baseball_number = RandomBaseballNumber.fromDigits()

    baseball_game = BaseballGame(random_baseball_number)
    baseball_game.play()
