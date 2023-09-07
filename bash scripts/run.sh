#!/bin/bash

chmod u+x run.sh
# Change directory to backend
cd ../backend
# Activate the environment
conda activate backend_coinbase_visualiser
# Start backend server
uvicorn coin_server:app --host localhost --port 8000 --workers 5 &
# Change directory to frontend
cd ../client-website
# Install dependencies with npm
npm start