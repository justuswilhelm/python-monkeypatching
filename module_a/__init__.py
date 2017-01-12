"""Module b."""


def method_a():
    """Print without override."""
    print("{}.method_a was called (no override)".format(__name__))


class Test:
    """."""

    def do_stuff(self):
        """Call method_a in the global() namespace of this module."""
        method_a()


def main():
    """Main."""
    print("--- In {}.main()".format(__name__))
    a = Test()
    a.do_stuff()
