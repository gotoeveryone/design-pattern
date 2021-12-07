from abc import ABCMeta, abstractmethod
from visitor.visitor import Visitor


class Element(metaclass=ABCMeta):
    @abstractmethod
    def get_label(self):
        pass

    @abstractmethod
    def get_time(self):
        pass

    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


class HogeElement(Element):
    def get_label(self):
        return 'hoge'

    def get_time(self):
        return '90m'

    def accept(self, visitor: Visitor):
        visitor.visit(self)


class FugaElement(Element):
    def get_label(self):
        return 'fuga'

    def get_time(self):
        return '6h'

    def accept(self, visitor: Visitor):
        visitor.visit(self)


class PiyoElement(Element):
    def get_label(self):
        return 'piyo'

    def get_time(self):
        return 'unknown'

    def accept(self, visitor: Visitor):
        visitor.visit(self)
