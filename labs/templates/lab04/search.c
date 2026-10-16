// Part A · search.c
// Read a SORTED list of integers and a target, then search for the target twice:
// once with linear search and once with binary search. Print the result of each
// and how many comparisons each one needed.
//
//   $ make search && ./search
//   How many numbers? 7
//   Number: 1
//   Number: 5
//   Number: 10
//   Number: 20
//   Number: 50
//   Number: 100
//   Number: 500
//   Target: 50
//   Linear: found at index 4 after 5 comparisons
//   Binary: found at index 4 after 3 comparisons
//
// If the target is missing, print e.g. "Linear: not found after 7 comparisons".
// Both functions return the INDEX of the target, or -1 when it is absent, and store the
// number of comparisons made in *comparisons (a pointer: write *comparisons = ...;
// we meet pointers properly in week 6, for now treat it as "the counter the caller gave you").
// You may assume 1 ≤ n ≤ 100 and that the numbers arrive in increasing order.

#include <cs50.h>
#include <stdio.h>

int linear_search(int n, int numbers[], int target, int *comparisons);
int binary_search(int n, int numbers[], int target, int *comparisons);

int main(void)
{
    int n = get_int("How many numbers? ");
    int numbers[n];
    for (int i = 0; i < n; i++)
    {
        numbers[i] = get_int("Number: ");
    }
    int target = get_int("Target: ");

    int c1 = 0;
    int i1 = linear_search(n, numbers, target, &c1);
    // TODO: print the Linear line

    int c2 = 0;
    int i2 = binary_search(n, numbers, target, &c2);
    // TODO: print the Binary line
}

// Look at every element from left to right; one comparison per element looked at.
int linear_search(int n, int numbers[], int target, int *comparisons)
{
    // TODO
    return -1;
}

// Halve the range each time; one comparison per middle element looked at.
int binary_search(int n, int numbers[], int target, int *comparisons)
{
    // TODO
    return -1;
}
