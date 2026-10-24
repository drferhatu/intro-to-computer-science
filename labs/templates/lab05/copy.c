// Part B · copy.c
// Read a string s, make a REAL copy t of it (new memory), uppercase every letter of the copy,
// print both, and free the copy. The original must stay unchanged.
//
//   $ make copy && ./copy
//   s: hello, world
//   s: hello, world
//   t: HELLO, WORLD
//
// Steps: malloc strlen(s) + 1 bytes (the +1 is for the '\0'); if malloc returns NULL, return 1;
// strcpy(t, s); loop over t with toupper; print; free(t). The checks run this program under
// valgrind: no invalid reads/writes and no leaks allowed.

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    string s = get_string("s: ");

    // TODO
    return 0;
}
