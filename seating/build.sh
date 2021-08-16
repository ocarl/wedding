#!/bin/sh
python create_seating.py && pdflatex seating.tex && open seating.pdf
