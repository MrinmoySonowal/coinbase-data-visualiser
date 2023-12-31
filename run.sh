#!/bin/bash

# Change directory to backend
cd backend
# Start backend server
uvicorn coin_server:app --host 0.0.0.0 --port 8000 --workers 5 &
# Change directory to frontend
cd ../client_website
# Install dependencies with npm
npm start
