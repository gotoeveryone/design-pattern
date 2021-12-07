from abc import ABCMeta, abstractmethod


class Visitor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self, acceptor):
        pass


class MyVisitor(Visitor):
    def visit(self, acceptor):
        class_name = acceptor.__class__.__name__
        if class_name == 'HogeElement':
            print(
                f'hoge 用の処理 [label: {acceptor.get_label()}] [time: {acceptor.get_time()}]')
        elif class_name == 'FugaElement':
            print(
                f'fuga 用の処理 [label: {acceptor.get_label()}] [time: {acceptor.get_time()}]')
        else:
            print('未実装！！')

    # オーバーロードが使える言語なら以下のように書ける
    # def visit(self, acceptor: HogeElement):
    #     print(f'hoge 用の処理 [label: {acceptor.get_label()}] [time: {acceptor.get_time()}]')

    # def visit(self, acceptor: FugaElement):
    #     print(f'fuga 用の処理 [label: {acceptor.get_label()}] [time: {acceptor.get_time()}]')
