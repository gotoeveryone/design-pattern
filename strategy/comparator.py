from abc import ABCMeta, abstractmethod
from decimal import Decimal, ROUND_HALF_UP

from strategy.entity import Person


class Comparator(metaclass=ABCMeta):
    @abstractmethod
    def compare(self, p1: Person, p2: Person):
        pass


class HeightComparator(Comparator):
    def compare(self, p1: Person, p2: Person):
        if p1.height == p2.height:
            return 0

        return 1 if p1.height > p2.height else -1


class AgeComparator(Comparator):
    def compare(self, p1: Person, p2: Person):
        # 10の位で四捨五入したうえで比較する
        p1_age = int(Decimal(p1.age).quantize(
            Decimal('1E1'), rounding=ROUND_HALF_UP))
        p2_age = int(Decimal(p2.age).quantize(
            Decimal('1E1'), rounding=ROUND_HALF_UP))

        if p1_age == p2_age:
            return 0

        return 1 if p1_age > p2_age else -1
