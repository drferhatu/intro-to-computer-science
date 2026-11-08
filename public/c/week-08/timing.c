// The same loop as timing.py, in C. Build with: gcc -o timing timing.c

#include <stdio.h>
#include <time.h>

int main(void)
{
    long n = 10000000;
    clock_t start = clock();
    long total = 0;
    for (long i = 0; i < n; i++)
    {
        total += i;
    }
    double seconds = (double) (clock() - start) / CLOCKS_PER_SEC;
    printf("for loop      %6.3f s   total = %ld\n", seconds, total);
}
