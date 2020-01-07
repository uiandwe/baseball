# -*- coding: utf-8 -*-

class Ball:
    min_ball_count = 0
    total_number_count = 3
    out_of_range_exception = "볼의 갯수가 올바르지 않습니다"

    def __init__(self, ball):
        self.valid_ball(ball)
        self.ball = ball

    def valid_ball(self, ball):
        if ball < Ball.min_ball_count or ball > Ball.total_number_count:
            raise Exception(Ball.out_of_range_exception)

    def exist(self):
        return self.ball > Ball.min_ball_count
