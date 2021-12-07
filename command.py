from abc import ABCMeta, abstractmethod


class BaseCommand(metaclass=ABCMeta):
    __name = "command"

    def __init__(self):
        pass

    @property
    def name(self):
        pass

    @name.getter
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @abstractmethod
    def run(self):
        pass
