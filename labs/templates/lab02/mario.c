// Part D · mario.c
// Print a right-aligned pyramid of '#' whose height the user chooses (1–8).
// Re-prompt until the height is valid. Each row i (counting from 1) has
// height - i spaces followed by i hashes, then a newline.
//
//   $ make mario && ./mario
//   Height: 4
//      #
//     ##
//    ###
//   ####
//
// Hints: a do-while for the input (see mario7.c from the lecture), then
// nested for loops: one for the rows, inside it one for spaces and one for hashes.

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: ask for the height until it is between 1 and 8
    int height = 0;

    // TODO: print the pyramid
}
