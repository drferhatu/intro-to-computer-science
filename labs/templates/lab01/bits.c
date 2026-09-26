// Part D · bits.c
// Ask for a number from 0 to 255 and print it as 8 bits, most significant first.
//
//   $ make bits && ./bits
//   Number (0–255): 73
//   01001001
//
// The loop below is already written. `bit` is 1 or 0 for each position, from 128 down to 1.
// Your job is the one line marked TODO: print the character '1' when bit is 1, else '0'.

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Number (0–255): ");
    }
    while (n < 0 || n > 255);

    for (int i = 7; i >= 0; i--)
    {
        int bit = (n >> i) & 1;   // shift the bits right i places, keep the last one

        // TODO: replace the two '?' with the right characters
        printf("%c", bit == 1 ? '?' : '?');
    }
    printf("\n");
}
