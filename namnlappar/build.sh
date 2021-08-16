#!/bin/sh
. ../venv/bin/activate
python create_name_tags.py && pdflatex tags.tex && open tags.pdf
