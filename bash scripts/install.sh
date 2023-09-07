#!/bin/bash

cd ../backend
# Install dependencies and conda env with conda
conda env create -f ENV.yml
cd ../client-website
# Install dependencies with npm
npm install