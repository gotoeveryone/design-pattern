from command import BaseCommand
from bridge.command import BridgeCommand
from visitor.command import VisitorCommand


class CommandFactory:
    _patterns = {
        "bridge": BridgeCommand,
        "visitor": VisitorCommand,
    }

    @classmethod
    def get_command(cls, pattern) -> BaseCommand:
        if pattern not in cls._patterns:
            raise Exception(f"invalid pattern: {pattern}")

        return cls._patterns.get(pattern)()
