#!/bin/sh
. ../venv/bin/activate
python3 create_menu.py && pdflatex menu_to_print.tex && pdflatex booklet.tex && open booklet.pdf
