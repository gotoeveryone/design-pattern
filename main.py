import sys

from factory import CommandFactory


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("too few argument")

    [_, pattern] = sys.argv
    command = CommandFactory.get_command(pattern)
    command.run()
