// Merge sort: sort the left half, sort the right half, merge the two sorted halves

#include <stdio.h>

void merge_sort(int a[], int left, int right, int depth);
void merge(int a[], int left, int middle, int right);
void print_range(int a[], int left, int right, int depth);

int main(void)
{
    int numbers[] = {6, 3, 8, 5, 2, 7, 4, 1};
    int n = 8;
    merge_sort(numbers, 0, n - 1, 0);
}

void merge_sort(int a[], int left, int right, int depth)
{
    // Base case: one element is already sorted
    if (left >= right)
    {
        return;
    }
    int middle = (left + right) / 2;
    merge_sort(a, left, middle, depth + 1);
    merge_sort(a, middle + 1, right, depth + 1);
    merge(a, left, middle, right);
    print_range(a, left, right, depth);
}

void merge(int a[], int left, int middle, int right)
{
    int tmp[right - left + 1];
    int i = left, j = middle + 1, k = 0;
    while (i <= middle && j <= right)
    {
        tmp[k++] = (a[i] <= a[j]) ? a[i++] : a[j++];
    }
    while (i <= middle)
    {
        tmp[k++] = a[i++];
    }
    while (j <= right)
    {
        tmp[k++] = a[j++];
    }
    for (k = 0; k < right - left + 1; k++)
    {
        a[left + k] = tmp[k];
    }
}

void print_range(int a[], int left, int right, int depth)
{
    for (int d = 0; d < depth; d++)
    {
        printf("  ");
    }
    printf("merged [%i..%i]: ", left, right);
    for (int i = left; i <= right; i++)
    {
        printf("%i ", a[i]);
    }
    printf("\n");
}
