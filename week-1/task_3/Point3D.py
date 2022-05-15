from __future__ import annotations
from task_2 import Point2D
import math


class Point3D(Point2D):
    def __init__(self, x: int | float, y: int | float, z: int | float):
        super().__init__(x, y)
        self.z = z

    def distance(self, other_point: Point3D):
        return math.sqrt(
            (self.x - other_point.x)**2
            + (self.y - other_point.y)**2
            + (self.z - other_point.z)**2
        )
