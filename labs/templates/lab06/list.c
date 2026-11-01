// Part A · list.c
// A linked list of integers. Read numbers until the user types 0, inserting each at the HEAD of the list
// (lecture: list3.c), then print the list, then search it for a target, then free every node (list6.c).
//
//   $ make list && ./list
//   Number (0 to stop): 1
//   Number (0 to stop): 2
//   Number (0 to stop): 3
//   Number (0 to stop): 0
//   List: 3 2 1
//   Target: 2
//   Found
//
// Print "Found" or "Not found". The checks run this program under valgrind: free every node.

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
} node;

node *insert_head(node *list, int number);
void print_list(node *list);
bool search(node *list, int target);
void free_list(node *list);

int main(void)
{
    node *list = NULL;

    // TODO: read numbers until 0, inserting each at the head

    printf("List:");
    print_list(list);
    printf("\n");

    int target = get_int("Target: ");
    printf(search(list, target) ? "Found\n" : "Not found\n");

    free_list(list);
    return 0;
}

// Returns the new head after inserting number at the front. Returns the old list if malloc fails.
node *insert_head(node *list, int number)
{
    // TODO
    return list;
}

// Prints every number, each preceded by one space: " 3 2 1"
void print_list(node *list)
{
    // TODO
}

bool search(node *list, int target)
{
    // TODO
    return false;
}

void free_list(node *list)
{
    // TODO
}
