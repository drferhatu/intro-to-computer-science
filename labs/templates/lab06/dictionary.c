// Part C · dictionary.c
// A hash table for a spell checker. speller.c (given) calls your four functions:
//   load(dictionary)  read every word of the file into the table (one node per word, insert at the head
//                     of its bucket); return true on success
//   check(word)       return true if word is in the table, ignoring case (strcasecmp from <strings.h>)
//   size()            how many words were loaded
//   unload()          free every node; return true
//
//   $ make speller && ./speller dictionaries/small texts/cat.txt
//   MISSPELLED WORDS
//   ...
//   WORDS MISSPELLED:     ...
//   WORDS IN DICTIONARY:  ...
//   WORDS IN TEXT:        ...
//
// Start with the lecture's hash function (first letter → 0–25) and N = 26 buckets; it works and passes.
// Then make it better: more buckets and a hash that uses more of the word, so that the lists stay
// short and lookups get faster. The notebook lets you compare how evenly different hash functions spread words.
// The checks run speller under valgrind: no leaks, no invalid reads.

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// One word in the table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Number of buckets in the hash table (change this when you improve the hash function).
// A #define, not a const int: C needs a true constant for the size of a global array.
#define N 26

// The hash table itself: an array of N pointers to linked lists
node *table[N];

// How many words have been loaded
unsigned int word_count = 0;

// Hashes a word to a number from 0 to N - 1
unsigned int hash(const char *word)
{
    // TODO: start with the lecture's hash, then improve it
    return toupper(word[0]) - 'A';
}

bool load(const char *dictionary)
{
    // TODO: open the file; read one word at a time with fscanf(file, "%s", buffer) until it returns EOF;
    //       for each word malloc a node, copy the word, prepend it to table[hash(word)], count it; fclose.
    return false;
}

unsigned int size(void)
{
    // TODO
    return 0;
}

bool check(const char *word)
{
    // TODO: walk the bucket for this word and compare case-insensitively
    return false;
}

bool unload(void)
{
    // TODO: free every node in every bucket
    return false;
}
