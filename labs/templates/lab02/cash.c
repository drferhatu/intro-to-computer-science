// Part F · cash.c
// Ask for an amount of change in cents (re-prompt if negative) and print the
// minimum number of coins needed, using quarters (25), dimes (10), nickels (5)
// and pennies (1). Always use the biggest coin that fits first: this is a greedy algorithm.
//
//   $ make cash && ./cash
//   Change owed: 41
//   4
//
// 41 = 25 + 10 + 5 + 1 → four coins.
// Hints: a do-while for the input; then a while loop per coin, or the / and % operators.

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: ask for the change until it is 0 or more
    int cents = 0;

    // TODO: count the coins and print the count
}
