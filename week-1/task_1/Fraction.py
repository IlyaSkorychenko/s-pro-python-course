from __future__ import annotations
import re
from .OperationsMixin import OperationsMixin


class Fraction(OperationsMixin):
    def __init__(self, num: int | float, den: int | float):
        self.__num = num
        self.__den = den

    @property
    def num(self):
        return self.__num

    @property
    def den(self) -> int | float:
        return self.__den

    @num.setter
    def num(self, value):
        self.__num = value

    @den.setter
    def den(self, value):
        assert value != 0, 'Denominator should be not zero'
        self.__den = value

    def __add__(self, other: Fraction):
        lcm_of_dens = self.lcm(self.den, other.den)

        self_num_multiplier = lcm_of_dens / self.den
        other_num_multiplier = lcm_of_dens / other.den

        return Fraction(
            (self.num * self_num_multiplier) + (other.num * other_num_multiplier),
            lcm_of_dens
        )

    def __sub__(self, other: Fraction):
        return self.__add__(Fraction(-other.num, other.den))

    def __mul__(self, other: Fraction):
        return Fraction(
            self.num * other.num,
            self.den * other.den
        )

    def __truediv__(self, other: Fraction):
        return self.__mul__(Fraction(other.den, other.num))

    def __str__(self):
        return f'{self.num}/{self.den}'

    @classmethod
    def init_from_string(cls, str_fraction: str):
        assert re.match('^\d+\/\d+$', str_fraction), 'Unexpected format, expect "number/number"'
        num, den = str_fraction.split('/')

        return cls(num, den)

    @staticmethod
    def gcd(a: int | float, b: int | float):
        assert a or b, 'Numbers must be not null'

        while b != 0:
            if a < b:
                temp = a % b
            else:
                temp = b % a
            a = b
            b = temp

        return a

    @staticmethod
    def lcm(a: int | float, b: int | float):
        return (a * b) / Fraction.gcd(a, b)
