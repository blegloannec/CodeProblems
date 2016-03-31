CC = ocamlc
FLAGS =
SOURCES = $(wildcard *.ml)
BINS = $(SOURCES:.ml=.out)

all: $(BINS)

%.out: %.ml
	$(CC) $< -o $@

clean:
	rm -f *.out *.cmo *.cmi *~
