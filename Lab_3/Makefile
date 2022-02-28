TEX_FILES = $(wildcard *.tex)
PDF_FILES = $(TEX_FILES:.tex=.pdf)

.PHONY: all clean pdf

all: pdf

pdf: $(PDF_FILES)

%.pdf: %.tex
	latexmk -pdf $<

clean:
	-rm -f $(PDF_FILES)
