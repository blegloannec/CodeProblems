CC = g++
CCC = gcc -lm
FLAGS = -Wall
SOURCES = $(wildcard *.cpp)
CSOURCES = $(wildcard *.c)
BINS = $(SOURCES:.cpp=.out) $(CSOURCES:.c=.out)

all: $(BINS)

%.out: %.cpp
	$(CC) $(FLAGS) $< -o $@

%.out: %.c
	$(CCC) $(FLAGS) -o $@ $< -lm

clean:
	rm -f *.out *~
