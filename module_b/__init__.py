"""."""
import module_a
from module_a import Test
from unittest.mock import patch


def method_b():
    """The method we want to patch module_a.method_a with."""
    print("{}.method_b was called (with override)".format(__name__))


def with_patch():
    """Patch method_a with method_b."""
    print("--- In {}.with_patch():".format(__name__))
    a = Test()
    with patch("module_a.method_a", new=method_b) as patched:
        print("Applying patch, {}.method_a == {}".format(__name__,
                                                         patched))
        a.do_stuff()
    print("Reverting patch, {}.method_a == {}".format(__name__,
                                                      module_a.method_a))
    a.do_stuff()


def with_namespace():
    """Override method_a in module_a namespace with method_b."""
    print("--- In {}.with_namespace():".format(__name__))
    a = Test()
    module_a.method_a = method_b
    a.do_stuff()
    # Caveat: This will not revert method_a to the original method_a.


def main():
    """."""
    with_patch()
    with_namespace()
