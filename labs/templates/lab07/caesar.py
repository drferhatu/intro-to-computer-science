# Part B · caesar.py
#
# The Caesar cipher from Lab 3, in Python. The key comes from the command line.
#
#   $ python caesar.py 13
#   plaintext:  HELLO, world
#   ciphertext: URYYB, jbeyq
#
# Rules (the same as Lab 3):
#   - exactly one command-line argument, made of digits only; otherwise print
#     "Usage: python caesar.py key" and exit with status 1
#   - rotate letters by key % 26, keep upper/lower case, leave everything else unchanged
#   - prompt "plaintext:  " (two spaces) and print "ciphertext: " followed by the result
#
# Hints: sys.argv, str.isdigit(), ord() and chr(), c.isupper() / c.islower()

import sys


def rotate(c, key):
    """Return the character c shifted by key positions; non-letters come back unchanged."""
    # TODO
    return c


def main():
    # TODO: check sys.argv and the key
    key = 0

    plaintext = input("plaintext:  ")
    # TODO: build the ciphertext with rotate() and print it
    print("ciphertext: ")


if __name__ == "__main__":
    main()
