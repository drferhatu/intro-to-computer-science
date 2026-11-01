// A binary search tree of numbers: smaller to the left, larger to the right

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *left;
    struct node *right;
} node;

node *insert(node *tree, int number);
bool search(node *tree, int number);
void print(node *tree);
void free_tree(node *tree);

int main(void)
{
    node *tree = NULL;

    // Insert in this order and the tree comes out balanced: 4 at the top, 2 and 6 below, then 1 3 5 7
    int numbers[] = {4, 2, 6, 1, 3, 5, 7};
    for (int i = 0; i < 7; i++)
    {
        tree = insert(tree, numbers[i]);
    }

    // In-order traversal prints the numbers sorted
    print(tree);
    printf("\n");

    int n = get_int("Number: ");
    printf(search(tree, n) ? "Found\n" : "Not found\n");

    free_tree(tree);
}

// Returns the (possibly new) root of the tree after inserting number
node *insert(node *tree, int number)
{
    if (tree == NULL)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return NULL;
        }
        n->number = number;
        n->left = NULL;
        n->right = NULL;
        return n;
    }
    if (number < tree->number)
    {
        tree->left = insert(tree->left, number);
    }
    else if (number > tree->number)
    {
        tree->right = insert(tree->right, number);
    }
    return tree;
}

// The lecture's search: one comparison per level, so about log2(n) steps when balanced
bool search(node *tree, int number)
{
    if (tree == NULL)
    {
        return false;
    }
    else if (number < tree->number)
    {
        return search(tree->left, number);
    }
    else if (number > tree->number)
    {
        return search(tree->right, number);
    }
    else
    {
        return true;
    }
}

void print(node *tree)
{
    if (tree == NULL)
    {
        return;
    }
    print(tree->left);
    printf("%i ", tree->number);
    print(tree->right);
}

void free_tree(node *tree)
{
    if (tree == NULL)
    {
        return;
    }
    free_tree(tree->left);
    free_tree(tree->right);
    free(tree);
}
