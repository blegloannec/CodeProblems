CC = g++
FLAGS = -Wall
SRC = $(wildcard *.cpp)
EXE = $(SRC:.cpp=.o)

all: $(EXE)

%.o: %.cpp
	$(CC) $(FLAGS) $< -o $@

clean:
	rm -f *.o *.in in* *.out out* *~
