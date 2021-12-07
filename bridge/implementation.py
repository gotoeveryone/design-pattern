from abc import ABCMeta, abstractmethod
from datetime import datetime


class FormatImpl(metaclass=ABCMeta):
    @abstractmethod
    def format(self, value: str):
        pass


class FormatIntImpl(FormatImpl):
    def format(self, value: str):
        return "{:,}".format(int(value))


class FormatDateImpl(FormatImpl):
    def format(self, value: str):
        return datetime.strptime(value, '%Y-%m-%d').strftime('%Y/%m/%d')
