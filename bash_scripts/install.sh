#!/bin/bash

cd ../backend
# Install dependencies and conda env with conda
pip install -r requirements.txt
cd ../client-website
# Install dependencies with npm
npm install