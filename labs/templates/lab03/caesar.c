// Part C · caesar.c
// Encrypt text with a Caesar cipher whose key comes from the command line:
//
//   $ make caesar && ./caesar 13
//   plaintext:  HELLO, world
//   ciphertext: URYYB, jbeyq
//
// Rules:
//   - Exactly one command-line argument, made only of digits. Otherwise print
//     "Usage: ./caesar key" and return 1 (an error exit code). Return 0 on success.
//   - Letters are shifted by key positions, wrapping around the alphabet (Z + 1 = A).
//     Uppercase stays uppercase, lowercase stays lowercase. Keys may be larger than 26.
//   - Anything that is not a letter (spaces, punctuation, digits) is printed unchanged.
//
// Hints: a letter minus 'A' (or 'a') is its position 0–25; add the key, take % 26,
// add 'A' back. isdigit(), isupper(), islower() live in <ctype.h>; atoi() in <stdlib.h>.

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string s);
char rotate(char c, int key);

int main(int argc, string argv[])
{
    // TODO: validate argc and argv[1]; print the usage message and return 1 if wrong

    // TODO: convert the key, read the plaintext, print "ciphertext: " followed by each rotated character

    return 0;
}

// Returns true if every character of s is a digit (and s is not empty)
bool only_digits(string s)
{
    // TODO
    return false;
}

// Returns c shifted by key positions if it is a letter, c itself otherwise
char rotate(char c, int key)
{
    // TODO
    return c;
}
