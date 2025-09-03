# ------------------------------------------------------------
# NOTE:
# The functions below (`say_hello` and `add`) are the generic
# examples provided in the IDS706 Python project template.
# They are kept here to demonstrate the project skeleton
# (Makefile, tests, CI/CD).
# Future versions of this repository may extend or replace
# these functions once a specific project definition is set.
# ------------------------------------------------------------


def say_hello(name: str) -> str:
    """Return a greeting message to students in the IDS class."""
    return f"Hello, {name}, welcome to Data Engineering Systems (IDS 706)!"


def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b
