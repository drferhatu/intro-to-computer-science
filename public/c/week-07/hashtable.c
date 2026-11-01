// A hash table of names: 26 buckets (A–Z), each bucket a linked list

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node
{
    char *name;
    struct node *next;
} node;

#define BUCKETS 26
node *table[BUCKETS];

unsigned int hash(const char *name);
bool insert(const char *name);
bool lookup(const char *name);
void unload(void);

int main(void)
{
    const char *names[] = {"Mario", "Luigi", "Peach", "Toad", "Yoshi", "Lakitu", "Link", "Zelda"};
    for (int i = 0; i < 8; i++)
    {
        insert(names[i]);
    }

    // Show which bucket each name landed in: L has three names, a collision chain
    for (int b = 0; b < BUCKETS; b++)
    {
        if (table[b] != NULL)
        {
            printf("%c:", 'A' + b);
            for (node *ptr = table[b]; ptr != NULL; ptr = ptr->next)
            {
                printf(" %s", ptr->name);
            }
            printf("\n");
        }
    }

    string s = get_string("Name: ");
    printf(lookup(s) ? "Found\n" : "Not found\n");
    unload();
}

// The lecture's hash function: the first letter, as a number 0–25
unsigned int hash(const char *name)
{
    return toupper(name[0]) - 'A';
}

bool insert(const char *name)
{
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        return false;
    }
    n->name = malloc(strlen(name) + 1);
    if (n->name == NULL)
    {
        free(n);
        return false;
    }
    strcpy(n->name, name);

    // Prepend to the bucket's list: O(1)
    unsigned int b = hash(name);
    n->next = table[b];
    table[b] = n;
    return true;
}

// Jump to the bucket, then walk only that short list
bool lookup(const char *name)
{
    for (node *ptr = table[hash(name)]; ptr != NULL; ptr = ptr->next)
    {
        if (strcasecmp(ptr->name, name) == 0)
        {
            return true;
        }
    }
    return false;
}

void unload(void)
{
    for (int b = 0; b < BUCKETS; b++)
    {
        node *ptr = table[b];
        while (ptr != NULL)
        {
            node *next = ptr->next;
            free(ptr->name);
            free(ptr);
            ptr = next;
        }
    }
}
