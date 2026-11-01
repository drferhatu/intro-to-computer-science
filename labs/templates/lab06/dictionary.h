// Declares a dictionary's functionality (the same interface as CS50's speller)

#ifndef DICTIONARY_H
#define DICTIONARY_H

#include <stdbool.h>

// Maximum length for a word (e.g., pneumonoultramicroscopicsilicovolcanoconiosis)
#define LENGTH 45

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary);

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void);

// Returns true if word is in dictionary, else false (case-insensitive)
bool check(const char *word);

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void);

#endif // DICTIONARY_H
