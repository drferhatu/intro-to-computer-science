// Part B · readability.c
// Read a text and print the U.S. school grade needed to read it, using the Coleman–Liau index:
//
//   index = 0.0588 * L - 0.296 * S - 15.8
//
// where L is the average number of LETTERS per 100 words and S the average number of SENTENCES
// per 100 words. Round the index to the nearest integer (use round() from <math.h>).
//   index < 1   → print "Before Grade 1"
//   index >= 16 → print "Grade 16+"
//   otherwise   → print "Grade N"
//
//   $ make readability && ./readability
//   Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
//   Grade 3
//
// Counting rules (the same as CS50's):
//   a letter   is any character for which isalpha() is true;
//   a word     is any sequence of characters separated by spaces, so words = spaces + 1
//              (assume the text has at least one word and no leading/trailing/double spaces);
//   a sentence ends with '.', '!' or '?'.
// Write the three counting functions, then compute the index in main.

#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");

    // TODO: count, compute L and S per 100 words, compute the index, print the grade
}

int count_letters(string text)
{
    // TODO
    return 0;
}

int count_words(string text)
{
    // TODO
    return 0;
}

int count_sentences(string text)
{
    // TODO
    return 0;
}
