// Part B · greet.c
// Ask for a name and print "hello, " followed by the name and a newline.
// get_string comes from cs50.h; it returns the text the user typed (a string).
//
//   $ make greet && ./greet
//   What's your name? Firat
//   hello, Firat

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string name = get_string("What's your name? ");

    // TODO: complete the printf. %s is the placeholder for a string; the value comes
    // after the format string, separated by a comma.
    printf("hello, \n");
}
