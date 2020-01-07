# -*- coding: utf-8 -*-
from Strike import Strike
from number.BaseballNumber import BaseballNumber
from number.BaseballDigit import BaseballDigit

class Rule:
    def __init__(self, answer):
        self.answer = answer
        self.is_end_game = False

    def guess(self, inputs):
        ball_count = BaseballNumber.get_ball_count(inputs, self.answer)
        self.check_max_strike(ball_count)
        return ball_count

    def check_max_strike(self, ball_count):
        if ball_count.is_max_strike():
            self.is_end_game = True
