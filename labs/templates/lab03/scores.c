// Part A · scores.c
// Read how many scores there are (1–10, re-prompt otherwise), then read that many
// integer scores into an array, and print the minimum, the maximum and the average:
//
//   $ make scores && ./scores
//   How many scores? 3
//   Score: 72
//   Score: 73
//   Score: 33
//   Min: 33
//   Max: 73
//   Average: 59.33
//
// Write THREE functions that take the array (and its length) and complete main.
// Remember: an array does not know its own length in C, so you pass it along.
// The average is a real number with two decimals: divide by (float) n.

#include <cs50.h>
#include <stdio.h>

int lowest(int n, int scores[]);
int highest(int n, int scores[]);
float average(int n, int scores[]);

int main(void)
{
    // TODO: ask "How many scores? " until the answer is between 1 and 10
    int n = 0;

    // TODO: declare an array of n ints and fill it with get_int("Score: ")

    // TODO: print Min, Max and Average using the three functions below
}

// Returns the smallest value in the array
int lowest(int n, int scores[])
{
    // TODO
    return 0;
}

// Returns the largest value in the array
int highest(int n, int scores[])
{
    // TODO
    return 0;
}

// Returns the average as a float
float average(int n, int scores[])
{
    // TODO
    return 0;
}
