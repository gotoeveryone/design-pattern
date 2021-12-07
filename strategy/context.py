from strategy.entity import Person


class Context:
    def __init__(self, comparator):
        self.comparator = comparator

    def compare(self, a1: Person, a2: Person):
        return self.comparator.compare(a1, a2)
