from command import BaseCommand
from bridge.function import Formatter, SafeFormatter
from bridge.implementation import FormatIntImpl, FormatDateImpl


class BridgeCommand(BaseCommand):
    def __init__(self):
        super(BaseCommand, self).__init__()
        self.name = "bridge"

    def run(self):
        formatter = Formatter(implementation=FormatIntImpl())
        print(formatter.format('12345'))

        formatter = SafeFormatter(implementation=FormatDateImpl())
        print(formatter.format('2021-05-02'))

        # 数値じゃないケースもあるからエラーにしたくないようなケースにおいて、
        # 機能（フォーマッタ）と実装を自由に組み合わせることができる
        formatter = SafeFormatter(implementation=FormatIntImpl())
        print(formatter.format('hogefuga'))  # エラーにならず None を返す
