// Selection sort: find the smallest of what is left, swap it to the front

#include <stdio.h>

void print_array(int n, int a[]);

int main(void)
{
    int numbers[] = {6, 3, 8, 5, 2, 7, 4, 1};
    int n = 8;
    print_array(n, numbers);

    for (int i = 0; i < n - 1; i++)
    {
        // Find the smallest element from i to the end
        int smallest = i;
        for (int j = i + 1; j < n; j++)
        {
            if (numbers[j] < numbers[smallest])
            {
                smallest = j;
            }
        }

        // Swap it into position i
        int tmp = numbers[i];
        numbers[i] = numbers[smallest];
        numbers[smallest] = tmp;

        print_array(n, numbers);
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
