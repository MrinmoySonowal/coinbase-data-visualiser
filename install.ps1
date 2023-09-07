# Change directory to backend
Set-Location ./backend
# Install dependencies with conda
conda env create -f ENV.yml
# Change directory to frontend
Set-Location ../client-website
# Install dependencies with npm
npm install