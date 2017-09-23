#!/bin/bash
sudo apt-get update -qq
sudo apt-get install -y --no-install-recommends \
    texlive-xetex texlive-latex-extra latex-xcolor\
    texlive-publishers texlive-lang-german \
    texlive-fonts-recommended lmodern fonts-sil-gentium-basic \
    python-pygments
