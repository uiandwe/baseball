# -*- coding: utf-8 -*-
class BaseballDigit:

    out_of_range_exception = "올바르지 않은 숫자 범위입니다."
    min_digit = 1
    max_digit = 9

    def __init__(self, digit):
        self._validate_digit(digit)
        self.digit = digit

    def _validate_digit(self, digit):
        if digit < BaseballDigit.min_digit or digit > BaseballDigit.max_digit:
            raise Exception(BaseballDigit.out_of_range_exception)

    def __eq__(self, other):
        if self.digit == other:
            return True
        if other is None:
            return False

        baseball_digit = BaseballDigit(other)
        return self.digit == baseball_digit.digit
