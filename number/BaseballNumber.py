# -*- coding: utf-8 -*-
from ballcount.Strike import Strike
from ballcount.Ball import Ball
from copy import deepcopy
from ballcount.BallCount import BallCount


class BaseballNumber:
    total_number_count = 3

    @staticmethod
    def get_ball_count(inputs, target):
        strike_count = BaseballNumber.get_strike_count(inputs, target)
        strike = Strike(strike_count)

        ball_count = BaseballNumber.get_ball(inputs, target)
        ball = Ball(ball_count)
        return BallCount(strike, ball)

    @staticmethod
    def view_target(target):
        return [o.digit for o in target]

    @staticmethod
    def get_strike_count(inputs, target):
        count = 0
        for input_num, target_num in zip(inputs, target):
            if int(input_num) == int(target_num.digit):
                count += 1
        return count

    @staticmethod
    def get_ball(inputs, target):
        count = 0
        for index, value in enumerate(target):
            remove_index_inputs = list(deepcopy(inputs))
            remove_index_inputs.pop(index)
            if str(value.digit) in remove_index_inputs:
                count += 1
        return count
