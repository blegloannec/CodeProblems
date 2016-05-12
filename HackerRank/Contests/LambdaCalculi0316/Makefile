CC = ocamlopt
FLAGS =
SOURCES = $(wildcard *.ml)
BINS = $(SOURCES:.ml=.out)

all: $(BINS)

alg_expr.out: alg_expr.ml
	$(CC) str.cmxa $< -o $@

%.out: %.ml
	$(CC) $< -o $@

clean:
	rm -f *.out *.cmo *.cmi *.cmx *.o *~
