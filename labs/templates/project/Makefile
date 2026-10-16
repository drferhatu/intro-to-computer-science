# Edit PROGRAM and the source list for your project. For Python or web projects you can delete this file.
CC = gcc
CFLAGS = -std=c11 -Wall -Wextra -g -Isrc
PROGRAM = program
SRC = $(wildcard src/*.c)

$(PROGRAM): $(SRC)
	$(CC) $(CFLAGS) -o $@ $(SRC) -lm

clean:
	rm -f $(PROGRAM) *.o
	rm -rf *.dSYM

.PHONY: clean
