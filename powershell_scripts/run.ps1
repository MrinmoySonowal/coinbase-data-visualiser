# Change directory to backend
Set-Location ./backend
# Activate the environment
conda activate backend-coinbase-visualiser
#Start backend servert
Start-Job -Name Backend -ScriptBlock {uvicorn coin_server:app --host localhost --port 8000 --workers 5}
# Change directory to frontend
Set-Location ../client-website
# Install dependencies with npm
npm start