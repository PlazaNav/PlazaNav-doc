#!/bin/bash
DATE=`date +"%y%m%d"`
JOBNAME="PlazaNav-$DATE"
# Shell escape is needed for pygments syntax highlighting
xelatex -shell-escape -jobname=$JOBNAME index.tex
# build bibliography
bibtex $JOBNAME.aux
# build again with bibliography
xelatex -shell-escape -jobname=$JOBNAME index.tex
# build a third time to fix potential numbering changes
xelatex -shell-escape -jobname=$JOBNAME index.tex
