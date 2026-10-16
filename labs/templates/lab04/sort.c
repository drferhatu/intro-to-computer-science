// Part B · sort.c
// Sort a list of integers with the algorithm named on the command line.
//
//   $ make sort && ./sort bubble
//   How many numbers? 5
//   Number: 6
//   Number: 3
//   Number: 8
//   Number: 1
//   Number: 2
//   1 2 3 6 8
//
// Rules:
//   - Exactly one argument, either "selection" or "bubble". Otherwise print
//     "Usage: ./sort selection|bubble" and return 1.
//   - Print the sorted numbers on ONE line, separated by single spaces, then a newline.
//   - selection_sort: for each position, find the smallest remaining element and swap it in.
//   - bubble_sort: compare neighbors and swap when out of order; stop early when a pass makes no swap.
// You may assume 1 ≤ n ≤ 100. strcmp (from <string.h>) compares two strings; it returns 0 when equal.

#include <cs50.h>
#include <stdio.h>
#include <string.h>

void selection_sort(int n, int numbers[]);
void bubble_sort(int n, int numbers[]);
void swap(int *a, int *b);

int main(int argc, string argv[])
{
    // TODO: validate the argument

    int n = get_int("How many numbers? ");
    int numbers[n];
    for (int i = 0; i < n; i++)
    {
        numbers[i] = get_int("Number: ");
    }

    // TODO: call the right sort, then print the numbers on one line

    return 0;
}

void selection_sort(int n, int numbers[])
{
    // TODO
}

void bubble_sort(int n, int numbers[])
{
    // TODO
}

// Swaps the two ints the pointers refer to. Call it as  swap(&numbers[i], &numbers[j]);
void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
