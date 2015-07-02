all: 
	pdflatex -synctex=1 -halt-on-error -file-line-error -interaction=nonstopmode -output-directory=output "thesis".tex 
	biber --output_directory output thesis 
	pdflatex -synctex=1 -interaction=nonstopmode -output-directory=output "thesis".tex
	open output/thesis.pdf
