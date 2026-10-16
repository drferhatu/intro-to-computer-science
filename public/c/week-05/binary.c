// Implements binary search for integers (the array must be sorted)

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // A sorted array of integers
    int numbers[] = {1, 5, 10, 20, 50, 100, 500};
    int size = 7;

    // Search for number
    int n = get_int("Number: ");
    int low = 0;
    int high = size - 1;
    int steps = 0;
    while (low <= high)
    {
        int middle = (low + high) / 2;
        steps++;
        printf("step %i: looking at index %i (%i)\n", steps, middle, numbers[middle]);
        if (numbers[middle] == n)
        {
            printf("Found after %i step(s)\n", steps);
            return 0;
        }
        else if (numbers[middle] < n)
        {
            low = middle + 1;
        }
        else
        {
            high = middle - 1;
        }
    }
    printf("Not found after %i step(s)\n", steps);
    return 1;
}
