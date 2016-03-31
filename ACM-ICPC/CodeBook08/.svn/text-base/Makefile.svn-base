name=PolyACM
tex_file=$(name).tex
pdf_file=$(name).pdf
others=$(wildcard Code/*/*.cc) $(wildcard Code/*/*.cpp)

all: $(pdf_file)

$(pdf_file): $(tex_file) $(others)
	pdflatex $<
	pdflatex $<


show: $(pdf_file)
	evince $<

xpdf: $(pdf_file)
	xpdf $<

acro: $(pdf_file)
	acroread $<

cons: $(pdf_file)
	fbgs $<

clean:
	rm -f $(pdf_file) *~ *.log *.aux *.toc *.bbl *.blg *.thm

