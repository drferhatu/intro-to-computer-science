// Minimal CS50-style library. See cs50.h. Do not edit for the labs.
#include <ctype.h>
#include <errno.h>
#include <limits.h>
#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cs50.h"

static string *allocations = NULL;
static size_t n_allocations = 0;

static void teardown(void)
{
    for (size_t i = 0; i < n_allocations; i++)
    {
        free(allocations[i]);
    }
    free(allocations);
}

static void vprompt(const char *format, va_list ap)
{
    if (format != NULL)
    {
        vprintf(format, ap);
        fflush(stdout);
    }
}

string get_string(const char *format, ...)
{
    va_list ap;
    va_start(ap, format);
    vprompt(format, ap);
    va_end(ap);

    size_t cap = 16, len = 0;
    char *buf = malloc(cap);
    if (buf == NULL)
    {
        return NULL;
    }
    int c;
    while ((c = fgetc(stdin)) != '\n' && c != EOF)
    {
        if (len + 1 >= cap)
        {
            cap *= 2;
            char *tmp = realloc(buf, cap);
            if (tmp == NULL)
            {
                free(buf);
                return NULL;
            }
            buf = tmp;
        }
        buf[len++] = (char) c;
    }
    if (len == 0 && c == EOF)
    {
        free(buf);
        return NULL;
    }
    buf[len] = '\0';

    string *tmp = realloc(allocations, (n_allocations + 1) * sizeof(string));
    if (tmp == NULL)
    {
        free(buf);
        return NULL;
    }
    allocations = tmp;
    if (n_allocations == 0)
    {
        atexit(teardown);
    }
    allocations[n_allocations++] = buf;
    return buf;
}

char get_char(const char *format, ...)
{
    va_list ap;
    while (true)
    {
        va_start(ap, format);
        vprompt(format, ap);
        va_end(ap);
        string line = get_string(NULL);
        if (line == NULL)
        {
            return CHAR_MAX;
        }
        char c, junk;
        if (sscanf(line, " %c %c", &c, &junk) == 1)
        {
            return c;
        }
    }
}

long get_long(const char *format, ...)
{
    va_list ap;
    while (true)
    {
        va_start(ap, format);
        vprompt(format, ap);
        va_end(ap);
        string line = get_string(NULL);
        if (line == NULL)
        {
            return LONG_MAX;
        }
        if (strlen(line) > 0 && !isspace((unsigned char) line[0]))
        {
            char *end;
            errno = 0;
            long n = strtol(line, &end, 10);
            if (errno == 0 && *end == '\0')
            {
                return n;
            }
        }
    }
}

int get_int(const char *format, ...)
{
    va_list ap;
    while (true)
    {
        va_start(ap, format);
        vprompt(format, ap);
        va_end(ap);
        string line = get_string(NULL);
        if (line == NULL)
        {
            return INT_MAX;
        }
        if (strlen(line) > 0 && !isspace((unsigned char) line[0]))
        {
            char *end;
            errno = 0;
            long n = strtol(line, &end, 10);
            if (errno == 0 && *end == '\0' && n >= INT_MIN && n <= INT_MAX)
            {
                return (int) n;
            }
        }
    }
}

double get_double(const char *format, ...)
{
    va_list ap;
    while (true)
    {
        va_start(ap, format);
        vprompt(format, ap);
        va_end(ap);
        string line = get_string(NULL);
        if (line == NULL)
        {
            return 0.0;
        }
        if (strlen(line) > 0 && !isspace((unsigned char) line[0]))
        {
            char *end;
            errno = 0;
            double d = strtod(line, &end);
            if (errno == 0 && *end == '\0')
            {
                return d;
            }
        }
    }
}

float get_float(const char *format, ...)
{
    va_list ap;
    va_start(ap, format);
    char prompt[256] = "";
    if (format != NULL)
    {
        vsnprintf(prompt, sizeof prompt, format, ap);
    }
    va_end(ap);
    return (float) get_double(format == NULL ? NULL : "%s", prompt);
}
