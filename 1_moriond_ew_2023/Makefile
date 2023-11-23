# Compile the latex code to produce a pdf and then delete the auxiliary files

base='presentation'

all:
	xelatex ${base}.tex
	xelatex ${base}.tex
	rm ${base}.aux
	rm ${base}.log 
	rm ${base}.toc
	rm ${base}.nav
	rm ${base}.out
	rm ${base}.snm
