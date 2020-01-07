# -*- coding: utf-8 -*-
import random

from .BaseballDigit import BaseballDigit
from .BaseballNumber import BaseballNumber


class RandomBaseballNumber:

    @staticmethod
    def fromDigits():
        baseball_digits = [BaseballDigit(x) for x in range(1, 10)]
        return baseball_digits

    def _next(self, random_baseball_number):
        random_baseball_number = self.shuffle(random_baseball_number)
        return random_baseball_number[0:BaseballNumber.total_number_count]

    def shuffle(self, random_baseball_number):
        random.shuffle(random_baseball_number)
        return random_baseball_number
