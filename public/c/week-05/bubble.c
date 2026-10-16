// Bubble sort: compare neighbors, swap if out of order, stop early if a pass makes no swap

#include <stdbool.h>
#include <stdio.h>

void print_array(int n, int a[]);

int main(void)
{
    int numbers[] = {6, 3, 8, 5, 2, 7, 4, 1};
    int n = 8;
    print_array(n, numbers);

    for (int pass = 0; pass < n - 1; pass++)
    {
        bool swapped = false;
        for (int j = 0; j < n - 1 - pass; j++)
        {
            if (numbers[j] > numbers[j + 1])
            {
                int tmp = numbers[j];
                numbers[j] = numbers[j + 1];
                numbers[j + 1] = tmp;
                swapped = true;
            }
        }
        print_array(n, numbers);
        if (!swapped)
        {
            break;   // already sorted: nothing moved in this pass
        }
    }
}

void print_array(int n, int a[])
{
    for (int i = 0; i < n; i++)
    {
        printf("%i ", a[i]);
    }
    printf("\n");
}
