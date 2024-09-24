from math import gcd
from dataclasses import dataclass


@dataclass(frozen=True)
class Fraction:
    numerator: int
    denominator: int

    def __post_init__(self):
        if self.denominator == 0:
            raise ZeroDivisionError("Denominator can't be zero")

        common_divisor = gcd(self.numerator, self.denominator)
        simplified_numerator = self.numerator // common_divisor
        simplified_denominator = self.denominator // common_divisor
        if simplified_denominator < 0:
            simplified_numerator = -simplified_numerator
            simplified_denominator = -simplified_denominator
        object.__setattr__(self, 'numerator', simplified_numerator)
        object.__setattr__(self, 'denominator', simplified_denominator)

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self) -> str:
        return f"Fraction({self.numerator}, {self.denominator})"

    def __add__(self, other: 'Fraction'):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
        elif isinstance(other, int):
            new_numerator = self.numerator + other * self.denominator
            new_denominator = self.denominator
        else:
            return NotImplemented
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other: 'Fraction'):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
        elif isinstance(other, int):
            new_numerator = self.numerator - other * self.denominator
            new_denominator = self.denominator
        else:
            return NotImplemented
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other: 'Fraction'):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
        elif isinstance(other, int):
            new_numerator = self.numerator * other
            new_denominator = self.denominator
        else:
            return NotImplemented
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other: 'Fraction'):
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError("Can't divide by zero")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
        elif isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("Can't divide by zero")
            new_numerator = self.numerator
            new_denominator = self.denominator * other
        else:
            return NotImplemented
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other: 'Fraction') -> bool:
        if isinstance(other, Fraction):
            return self.numerator == other.numerator and self.denominator == other.denominator
        elif isinstance(other, int):
            return self.numerator == other * self.denominator
        else:
            return NotImplemented

    def __lt__(self, other: 'Fraction') -> bool:
        if isinstance(other, Fraction):
            return self.numerator * other.denominator < other.numerator * self.denominator
        elif isinstance(other, int):
            return self.numerator < other * self.denominator
        else:
            return NotImplemented

    def __le__(self, other: 'Fraction') -> bool:
        return self < other or self == other

    def __gt__(self, other: 'Fraction') -> bool:
        return not self <= other

    def __ge__(self, other: 'Fraction') -> bool:
        return not self < other

    def __ne__(self, other: 'Fraction') -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((self.numerator, self.denominator))

    def __float__(self) -> float:
        return self.numerator / self.denominator

    def __int__(self) -> int:
        return self.numerator // self.denominator

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)


    def mixed_numbers(self) -> str:
        whole = self.numerator / self.denominator
        remainder = abs(self.numerator) % self.denominator
        if remainder < 0:
            return str(whole)
        elif whole == 0:
            return f"{remainder}/{self.denominator}"
        else:
            return f"{whole} {remainder}/{self.denominator}"


    def __iadd__(self, other: 'Fraction'):
        return self.__add__(other)

    def __isub__(self, other: 'Fraction'):
        return self.__sub__(other)

    def __imul__(self, other: 'Fraction'):
        return self.__mul__(other)

    def __itruediv__(self, other: 'Fraction'):
        return self.__truediv__(other)
