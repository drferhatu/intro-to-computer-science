# make scores  → compiles scores.c (plus the CS50 library) into ./scores
CC = gcc
CFLAGS = -std=c11 -Wall -Wextra -Wno-unused-parameter -g -I.

PROGRAMS = scores readability caesar

all: $(PROGRAMS)

%: %.c cs50.c cs50.h
	$(CC) $(CFLAGS) -o $@ $< cs50.c

clean:
	rm -f $(PROGRAMS) *.o
	rm -rf *.dSYM

.PHONY: all clean
