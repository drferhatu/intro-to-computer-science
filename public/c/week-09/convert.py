# convert.py · a MODULE: functions only, no input(), no print(). Other files import it.

def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def describe(celsius):
    """Return a one-word description of a temperature in Celsius."""
    if celsius < 0:
        return "freezing"
    if celsius < 12:
        return "cold"
    if celsius < 25:
        return "mild"
    return "hot"
