# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from number.RandomBaseballNumber import RandomBaseballNumber
from ballcount.Rule import Rule
from number.BaseballDigit import BaseballDigit

class BaseballGame:
    exception_user_number_range = "잘못된 입력값 입니다.(입력값 : 1~9)"
    exception_user_number_duplicate = "입력값에 중복값이 있습니다."

    def __init__(self, random_baseball_number):
        self.random_baseball_number = random_baseball_number
        self.is_end_game = False

    def play(self):
        rule = self.generate_rule()
        self.guess(rule)

    def generate_rule(self):
        random_baseball_number = RandomBaseballNumber()
        answer = random_baseball_number._next(self.random_baseball_number)
        return Rule(answer)

    def guess(self, rule):
        while not rule.is_end_game:
            user_generate_number = raw_input()
            self.valid_user_generate_number(user_generate_number)
            ball_count = rule.guess(user_generate_number)
            print(ball_count.to_string())

    def valid_user_generate_number(self, user_generate_number):
        for number in user_generate_number:
            if int(number) < BaseballDigit.min_digit or int(number) > BaseballDigit.max_digit:
                raise Exception(BaseballGame.exception_user_number_range)

            if user_generate_number.count(number) > 1:
                raise Exception(BaseballGame.exception_user_number_duplicate)

