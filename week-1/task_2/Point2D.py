from __future__ import annotations
import math


class Point2D:
    _amount_of_instances = 0

    def __init__(self, x: int | float, y: int | float):
        self.x = x
        self.y = y
        Point2D._amount_of_instances += 1

    def distance(self, other_point: Point2D):
        return math.sqrt(
            (self.x - other_point.x)**2 + (self.y - other_point.y)**2
        )

    @classmethod
    @property
    def amount_of_instances(cls):
        return cls._amount_of_instances
