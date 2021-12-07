from command import BaseCommand
from visitor.element import HogeElement, FugaElement, PiyoElement
from visitor.visitor import MyVisitor


class VisitorCommand(BaseCommand):
    def __init__(self):
        super(BaseCommand, self).__init__()
        self.name = "visitor"

    def run(self):
        # Visitor 側の実装と Element を追加することでパターンを追加できる
        # パターン追加によって Element クラスの実装を変更しなくて良くなる
        visitor = MyVisitor()
        element = HogeElement()
        element.accept(visitor)

        element = FugaElement()
        element.accept(visitor)

        element = PiyoElement()
        element.accept(visitor)
