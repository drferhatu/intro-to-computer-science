// Part E · calculator.c
// Read two integers x and y and print, each on its own line:
//   x + y
//   x - y
//   x * y
//   x / y   as a real number with two decimals   (or the text  undefined  when y is 0)
//   x % y   the remainder                         (or the text  undefined  when y is 0)
//
//   $ make calculator && ./calculator
//   x: 7
//   y: 2
//   9
//   5
//   14
//   3.50
//   1
//
// Hints: integer division truncates, so cast before dividing: (float) x / (float) y.
// printf("%.2f\n", z) prints two decimals. Use an if for the y == 0 case.

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x = get_int("x: ");
    int y = get_int("y: ");

    // TODO
}
