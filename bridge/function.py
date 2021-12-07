from bridge.implementation import FormatIntImpl


class Formatter():
    def __init__(self, implementation: FormatIntImpl):
        self._implementation = implementation

    def format(self, value: str):
        return self._implementation.format(value)


class SafeFormatter(Formatter):
    def format(self, value: str):
        try:
            return self._implementation.format(value)
        except:
            print('error')

        return None
