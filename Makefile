ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  # Unix
  pwd := $$(pwd)
  translate = $1
else
  # Windows mit MSys2/Cygwin
  pwd := $$(cygpath -m "$$(pwd)")
  translate = $(shell echo '$1' | sed 's/:/;/g')
endif

all: build/main.pdf

SRC = $(wildcard content/*tab.txt)
TAB = $(patsubst content/%tab.txt, build/%.tex, $(SRC))
PY = $(wildcard *t.py)
PLOT = $(patsubst %t.py, build/%t.pdf, $(PY))

# hier Python-Skripte (alle skripte müssen mit t.py enden):
build/%t.pdf: %t.py matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python &<

build/%.tex: content/%tab.txt tab.py
	TEXINPUTS="$(call translate,$(pwd):)" python tab.py $<

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: $(PLOT) $(TAB)

build/main.pdf: FORCE | build
	  TEXINPUTS="$(call translate,build:)" \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
