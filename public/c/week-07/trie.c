// A trie of names: a tree where every node has 26 children, one per letter

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node
{
    struct node *children[26];
    bool is_word;           // true if a name ends here
} node;

node *new_node(void);
bool insert(node *trie, const char *word);
bool search(node *trie, const char *word);
void unload(node *trie);

int main(void)
{
    node *trie = new_node();
    if (trie == NULL)
    {
        return 1;
    }

    // "Toad" and "Tom" share the T and the O
    insert(trie, "Toad");
    insert(trie, "Tom");
    insert(trie, "Toadette");

    string s = get_string("Name: ");
    printf(search(trie, s) ? "Found\n" : "Not found\n");
    unload(trie);
}

node *new_node(void)
{
    node *n = calloc(1, sizeof(node));   // calloc zeroes everything: all children NULL, is_word false
    return n;
}

// Walk letter by letter, creating nodes where the path does not exist yet
bool insert(node *trie, const char *word)
{
    node *ptr = trie;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        int c = toupper(word[i]) - 'A';
        if (c < 0 || c >= 26)
        {
            return false;
        }
        if (ptr->children[c] == NULL)
        {
            ptr->children[c] = new_node();
            if (ptr->children[c] == NULL)
            {
                return false;
            }
        }
        ptr = ptr->children[c];
    }
    ptr->is_word = true;
    return true;
}

// Search costs one step per letter of the word, no matter how many words are stored
bool search(node *trie, const char *word)
{
    node *ptr = trie;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        int c = toupper(word[i]) - 'A';
        if (c < 0 || c >= 26 || ptr->children[c] == NULL)
        {
            return false;
        }
        ptr = ptr->children[c];
    }
    return ptr->is_word;
}

void unload(node *trie)
{
    if (trie == NULL)
    {
        return;
    }
    for (int i = 0; i < 26; i++)
    {
        unload(trie->children[i]);
    }
    free(trie);
}
