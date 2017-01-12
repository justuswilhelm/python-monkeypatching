# Python 3 Namespace Monkey Patching

This shows two examples of replacing a value being referenced in a namespace.
Using

- `unittest.mock.patch`,
- and regular attribute setting on a module.

The monkey patching code can be found in `module_b/__init__.py`, the code being
monkey patched can be found in `module_a/__init__.py`.

To test, run

```bash
python3 run.py
```

This will print

```
--- In module_a.main()
method_a was called (no override)
--- In module_b.with_patch():
Applying patch, module_b.method_a == <function method_b at 0x107b39b70>
method_b was called (with override)
Reverting patch, module_b.method_a == <function method_a at 0x107b39a60>
method_a was called (no override)
--- In module_b.with_namespace():
method_b was called (with override)
```
