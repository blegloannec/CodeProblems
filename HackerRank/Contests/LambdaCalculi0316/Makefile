CC = ocamlopt
FLAGS =
SOURCES = $(wildcard *.ml)
BINS = $(SOURCES:.ml=.out)

all: $(BINS)

simplify_the_algebraic_expressions.out: simplify_the_algebraic_expressions.ml
	$(CC) str.cmxa $< -o $@

%.out: %.ml
	$(CC) $< -o $@

clean:
	rm -f *.out *.cmo *.cmi *.cmx *.o *~
