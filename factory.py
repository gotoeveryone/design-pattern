from command import BaseCommand
from visitor.command import VisitorCommand


class CommandFactory:
    @classmethod
    def get_command(cls, pattern) -> BaseCommand:
        if pattern == "visitor":
            return VisitorCommand()

        raise Exception(f"invalid pattern: {pattern}")
