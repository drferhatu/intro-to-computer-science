// Part C · recursion.c
// Two functions that call themselves.
//
//   $ make recursion && ./recursion
//   Height: 3
//   #
//   ##
//   ###
//   n: 5
//   5! = 120
//
// draw(n) prints a left-aligned pyramid of height n, recursively: a pyramid of height n is a
// pyramid of height n - 1 followed by one row of n hashes. A height of 0 or less prints nothing.
// factorial(n) returns n × (n-1) × … × 1, recursively, with factorial(0) = 1. Use long so that
// 20! still fits. No loops inside factorial; one loop (for the row of hashes) is fine inside draw.
// Re-prompt while the height is negative or above 20, and while n is negative or above 20.

#include <cs50.h>
#include <stdio.h>

void draw(int n);
long factorial(int n);

int main(void)
{
    // TODO: read the height (0–20), call draw

    // TODO: read n (0–20), print "n! = value" with %li
}

void draw(int n)
{
    // TODO
}

long factorial(int n)
{
    // TODO
    return 0;
}
