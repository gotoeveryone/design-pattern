from abc import ABCMeta, abstractmethod


class BaseCommand(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        pass
