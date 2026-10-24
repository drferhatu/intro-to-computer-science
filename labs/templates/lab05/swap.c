// Part A · swap.c
// The swap below does not work: it swaps two COPIES and leaves x and y alone (lecture: swap0.c).
// Change the function (its prototype, its parameters, its body) and the call in main so that it
// swaps the caller's variables through their ADDRESSES (lecture: swap1.c).
//
//   $ make swap && ./swap
//   x: 1
//   y: 2
//   x is 1, y is 2
//   x is 2, y is 1

#include <cs50.h>
#include <stdio.h>

void swap(int a, int b);

int main(void)
{
    int x = get_int("x: ");
    int y = get_int("y: ");

    printf("x is %i, y is %i\n", x, y);
    swap(x, y);
    printf("x is %i, y is %i\n", x, y);
}

void swap(int a, int b)
{
    int tmp = a;
    a = b;
    b = tmp;
}
