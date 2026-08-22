CFLAGS = -Wall -Wextra -pedantic

all: main

main: main.o
		gcc $(CFLAGS) main.o -o main

main.o: main.c
		gcc $(CFLAGS) -c main.c -o main.o

clean:
	rm *.o main

.PHONY: all clean
