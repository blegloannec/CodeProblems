CC=g++
CFLAGS=-Wall -O2
SRC=bellman_ford.cpp dijkstra.cpp dijkstra_custom_heap.cpp desopo_pape.cpp bench.cpp

bench: $(SRC)
	$(CC) $(CFLAGS) $(SRC) -o $@

clean:
	rm -f bench *.out *~
