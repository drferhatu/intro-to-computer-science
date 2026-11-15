# main.py · the PROGRAM: talks to the user, calls the module
# Run:  python main.py 21.5

import sys

from convert import celsius_to_fahrenheit, describe


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python main.py celsius")
    try:
        celsius = float(sys.argv[1])
    except ValueError:
        sys.exit("celsius must be a number")
    print(f"{celsius} °C = {celsius_to_fahrenheit(celsius):.1f} °F, {describe(celsius)}")


if __name__ == "__main__":
    main()
