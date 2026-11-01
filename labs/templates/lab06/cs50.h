// Minimal CS50-style library for this course's labs.
// Same names as Harvard's libcs50 (get_string, get_int, get_float, get_long, get_char, string, bool),
// implemented in cs50.c so that it compiles anywhere: Codespaces, Colab, your laptop.
#ifndef CS50_H
#define CS50_H

#include <stdbool.h>

typedef char *string;

// Prompts the user with the format string and returns the line typed, without the newline.
// Returns NULL at end of input. Memory is freed automatically at exit.
string get_string(const char *format, ...);

// Prompt again until the user types a valid value of the type.
char get_char(const char *format, ...);
int get_int(const char *format, ...);
long get_long(const char *format, ...);
float get_float(const char *format, ...);
double get_double(const char *format, ...);

#endif
