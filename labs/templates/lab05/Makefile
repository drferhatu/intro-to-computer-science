# make swap  → compiles swap.c (plus the CS50 library) into ./swap
CC = gcc
CFLAGS = -std=c11 -Wall -Wextra -Wno-unused-parameter -g -I.

PROGRAMS = swap copy leaks filter

all: $(PROGRAMS)

%: %.c cs50.c cs50.h bmp.h
	$(CC) $(CFLAGS) -o $@ $< cs50.c -lm

clean:
	rm -f $(PROGRAMS) *.o
	rm -rf *.dSYM

.PHONY: all clean
