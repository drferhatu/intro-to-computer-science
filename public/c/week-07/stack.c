// A stack of people with a fixed capacity: last in, first out (a pile of cafeteria trays)

#include <cs50.h>
#include <stdio.h>

#define CAPACITY 50

typedef struct
{
    string people[CAPACITY];
    int size;       // how many trays are on the pile
} stack;

void push(stack *s, string name);
string pop(stack *s);

int main(void)
{
    stack s = {.size = 0};

    push(&s, "Mario");
    push(&s, "Luigi");
    push(&s, "Peach");

    // The last one placed is the first one taken
    while (s.size > 0)
    {
        printf("%s leaves\n", pop(&s));
    }
}

void push(stack *s, string name)
{
    if (s->size == CAPACITY)
    {
        printf("The stack is full\n");
        return;
    }
    s->people[s->size] = name;
    s->size++;
}

string pop(stack *s)
{
    s->size--;
    return s->people[s->size];
}
