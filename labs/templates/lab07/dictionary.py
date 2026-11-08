# Part C · dictionary.py
#
# The spell checker's dictionary from Lab 6, in Python. speller.py (given, do not edit) imports
# these four functions and calls them exactly as speller.c called your dictionary.c.
#
#   $ python speller.py dictionaries/small texts/cat.txt
#
# Rules:
#   load(path)  reads the dictionary file (one word per line, lowercase) into a set; returns True,
#               or False if the file cannot be opened
#   check(word) returns True if the word is in the dictionary, ignoring case ("Cat" and "cat" are both correct)
#   size()      returns the number of words loaded (0 before load)
#   unload()    returns True (Python frees the memory itself)
#
# Hints: a set is a hash table; file.read().splitlines(); word.lower() in words

# The words, shared by all four functions
words = set()


def check(word):
    """Return True if word is in the dictionary, else False."""
    # TODO
    return False


def load(dictionary):
    """Load the dictionary into memory, returning True if successful, else False."""
    # TODO
    return False


def size():
    """Return the number of words in the dictionary if loaded, else 0."""
    # TODO
    return 0


def unload():
    """Unload the dictionary from memory, returning True if successful, else False."""
    # TODO
    return False
