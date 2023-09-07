#!/bin/bash

chmod u+x install.sh
cd ../backend
# Install dependencies with conda
conda env create -f ENV.yml
cd ../client-website
# Install dependencies with npm
npm install