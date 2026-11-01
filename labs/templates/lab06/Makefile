# make list  → ./list      make queue → ./queue      make speller → ./speller (your dictionary.c + the given speller.c)
CC = gcc
CFLAGS = -std=c11 -Wall -Wextra -Wno-unused-parameter -g -I.

all: list queue speller

list: list.c cs50.c cs50.h
	$(CC) $(CFLAGS) -o list list.c cs50.c

queue: queue.c cs50.c cs50.h
	$(CC) $(CFLAGS) -o queue queue.c cs50.c

speller: speller.c dictionary.c dictionary.h
	$(CC) $(CFLAGS) -o speller speller.c dictionary.c

clean:
	rm -f list queue speller *.o
	rm -rf *.dSYM

.PHONY: all clean
