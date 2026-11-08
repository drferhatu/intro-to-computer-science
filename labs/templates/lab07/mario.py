# Part A · mario.py
#
# The right-aligned pyramid from Lab 2, in Python.
#
#   $ python mario.py
#   Height: 4
#      #
#     ##
#    ###
#   ####
#
# Rules (the same as Lab 2):
#   - prompt exactly "Height: "
#   - keep asking until the user types an integer from 1 to 8 (re-prompt on "cat", 0, 9, -3 ...)
#   - row i (counting from 0) is  (height - i - 1) spaces  followed by  (i + 1) hashes
#
# Hints: int(input("Height: ")) inside try / except ValueError;  " " * n  and  "#" * n


def main():
    # TODO: ask for the height until it is valid
    height = 0

    # TODO: print the pyramid
    pass


if __name__ == "__main__":
    main()
