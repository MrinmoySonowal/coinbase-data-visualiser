#!/bin/bash

# Change directory to backend
cd ../backend
# Start backend server
uvicorn coin_server:app --host localhost --port 8000 --workers 5 &
# Change directory to frontend
cd ../client-website
# Install dependencies with npm
npm start