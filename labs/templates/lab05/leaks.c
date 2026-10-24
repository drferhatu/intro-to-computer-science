// Part C · leaks.c
// This program should read n (1–100), build an array of the numbers 1..n on the HEAP, and print
// their sum. It compiles, and it may even print the right answer, but it has THREE memory bugs.
// Run it under valgrind, read the report, and fix all three without changing what it prints.
//
//   $ make leaks && valgrind ./leaks
//   n: 4
//   sum = 10
//   ... HEAP SUMMARY: ... All heap blocks were freed -- no leaks are possible
//   ... ERROR SUMMARY: 0 errors from 0 contexts
//
// Hints: how many BYTES does malloc need for n ints? Where does the loop stop? What is missing at the end?

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("n: ");
    }
    while (n < 1 || n > 100);

    int *numbers = malloc(n);
    if (numbers == NULL)
    {
        return 1;
    }

    for (int i = 0; i <= n; i++)
    {
        numbers[i] = i + 1;
    }

    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += numbers[i];
    }
    printf("sum = %i\n", sum);
    return 0;
}
