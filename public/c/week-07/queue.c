// A queue of people with a fixed capacity: first in, first out (an amusement-park line)

#include <cs50.h>
#include <stdio.h>

#define CAPACITY 50

typedef struct
{
    string people[CAPACITY];
    int front;      // index of the first person in line
    int size;       // how many people are in line
} queue;

void enqueue(queue *q, string name);
string dequeue(queue *q);

int main(void)
{
    queue q = {.front = 0, .size = 0};

    enqueue(&q, "Mario");
    enqueue(&q, "Luigi");
    enqueue(&q, "Peach");

    // The ride takes people in the order they arrived
    while (q.size > 0)
    {
        printf("%s rides\n", dequeue(&q));
    }
}

void enqueue(queue *q, string name)
{
    if (q->size == CAPACITY)
    {
        printf("The line is full\n");
        return;
    }
    q->people[(q->front + q->size) % CAPACITY] = name;
    q->size++;
}

string dequeue(queue *q)
{
    string name = q->people[q->front];
    q->front = (q->front + 1) % CAPACITY;
    q->size--;
    return name;
}
