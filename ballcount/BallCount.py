# -*- coding: utf-8 -*-
class BallCount:
    strike_and_ball_format = "{} 스트라이크 {} 볼"
    only_strike_format = "{} 스트라이크"
    only_ball_format = "{} 볼"
    nothing = "낫싱"

    def __init__(self, strike, ball):
        self.strike = strike
        self.ball = ball

    def is_max_strike(self):
        return self.strike.is_max_strike()

    def to_string(self):
        if self.strike.exist_strike() and self.ball.exist():
            return BallCount.strike_and_ball_format.format(self.strike.strike, self.ball.ball)

        if self.strike.exist_strike():
            return BallCount.only_strike_format.format(self.strike.strike)

        if self.ball.exist():
            return BallCount.only_ball_format.format(self.ball.ball)

        return BallCount.nothing




