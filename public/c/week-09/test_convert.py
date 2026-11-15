# test_convert.py · tests for convert.py. Run them all with:  pytest
# pytest finds every file named test_*.py and every function named test_*, and runs them.

from convert import celsius_to_fahrenheit, describe


def test_freezing_and_boiling():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212


def test_minus_forty_is_the_same_in_both():
    assert celsius_to_fahrenheit(-40) == -40


def test_describe_boundaries():
    assert describe(-1) == "freezing"
    assert describe(0) == "cold"        # 0 is not below 0
    assert describe(11.9) == "cold"
    assert describe(12) == "mild"
    assert describe(25) == "hot"
