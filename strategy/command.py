from command import BaseCommand
from strategy.comparator import AgeComparator, HeightComparator
from strategy.context import Context
from strategy.entity import Person


class StrategyCommand(BaseCommand):
    def __init__(self):
        super(BaseCommand, self).__init__()
        self.name = "strategy"

    def run(self):
        a1 = Person(height=124, weight=53, age=25)
        a2 = Person(height=125, weight=60, age=30)
        a3 = Person(height=124, weight=45, age=20)

        # height でソートする
        context1 = Context(comparator=HeightComparator())
        comparator_class_name1 = context1.comparator.__class__.__name__
        print(
            f"{comparator_class_name1}でa1({a1.height})とa2({a2.height})を比較: {context1.compare(a1, a2)}")
        print(
            f"{comparator_class_name1}でa2({a2.height})とa3({a3.height})を比較: {context1.compare(a2, a3)}")
        print(
            f"{comparator_class_name1}でa1({a1.height})とa3({a3.height})を比較: {context1.compare(a1, a3)}")

        # age でソートするよう実装を差し替え
        context2 = Context(comparator=AgeComparator())
        comparator_class_name2 = context2.comparator.__class__.__name__
        print(
            f"{comparator_class_name2}でa1({a1.age})とa2({a2.age})を比較: {context2.compare(a1, a2)}")
        print(
            f"{comparator_class_name2}でa2({a2.age})とa3({a3.age})を比較: {context2.compare(a2, a3)}")
        print(
            f"{comparator_class_name2}でa1({a1.age})とa3({a3.age})を比較: {context2.compare(a1, a3)}")
