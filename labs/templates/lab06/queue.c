// Part B · queue.c
// A queue of names with a fixed capacity (lecture: queue.c). Read commands until "quit":
//   add NAME   → enqueue NAME at the back; print "Full" if there is no room
//   next       → dequeue the front name and print it; print "Empty" if nobody is waiting
//   quit       → stop
//
//   $ make queue && ./queue
//   > add Mario
//   > add Luigi
//   > next
//   Mario
//   > next
//   Luigi
//   > next
//   Empty
//   > quit
//
// Keep the queue circular: use front and size, and (front + size) % CAPACITY for the next free slot,
// so that adding and removing many times never runs off the end of the array.

#include <cs50.h>
#include <stdio.h>
#include <string.h>

#define CAPACITY 4

typedef struct
{
    string people[CAPACITY];
    int front;
    int size;
} queue;

bool enqueue(queue *q, string name);
string dequeue(queue *q);

int main(void)
{
    queue q = {.front = 0, .size = 0};
    while (true)
    {
        string cmd = get_string("> ");
        if (cmd == NULL || strcmp(cmd, "quit") == 0)
        {
            break;
        }
        // TODO: handle "add NAME" and "next"
    }
    return 0;
}

// Returns false (and changes nothing) when the queue is full
bool enqueue(queue *q, string name)
{
    // TODO
    return false;
}

// Returns NULL when the queue is empty
string dequeue(queue *q)
{
    // TODO
    return NULL;
}
