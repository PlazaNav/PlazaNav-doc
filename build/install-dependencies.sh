#!/bin/bash
sudo apt-get update -qq
sudo apt-get install -y --no-install-recommends \
    texlive-xetex texlive-latex-extra \
    texlive-publishers texlive-lang-german \
    lmodern fonts-sil-gentium-basic \
    python-pygments
