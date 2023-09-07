# Change directory to backend
Set-Location ./backend
# Install dependencies with conda
conda env create -f environment.yml
# Activate conda environment
conda activate backend-coinbase-visualiser
# Start backend server with uvicorn in a new job
Start-Job -Name Backend -ScriptBlock {uvicorn coin_server:app --host localhost --port 8000 --workers 5}
# Change directory to frontend
Set-Location ../frontend
# Install dependencies with npm
npm install
# Start frontend app with npm in a new job
Start-Job -Name Frontend -ScriptBlock {npm start}
# Wait for any job to finish
Wait-Job -Any
# Stop and remove all jobs
Stop-Job -Name Backend, Frontend
Remove-Job -Name Backend, Frontend