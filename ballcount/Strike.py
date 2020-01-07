# -*- coding: utf-8 -*-

class Strike:
    out_of_range_exception = "스트라이크의 갯수가 올바르지 않습니다"
    min_strike_count = 0
    total_number_count = 3

    def __init__(self, strike):
        self.valid_strike(strike)
        self.strike = strike

    def valid_strike(self, strike):
        if strike < Strike.min_strike_count or strike > Strike.total_number_count:
            raise Exception(Strike.out_of_range_exception)

    def is_max_strike(self):
        return self.strike == Strike.total_number_count

    def exist_strike(self):
        return self.strike > Strike.min_strike_count
