@echo off
echo ========================================
echo    Starting Nexus AI Backend Server
echo ========================================
echo.

cd /d "%~dp0backend"

echo Checking Python...
python --version
echo.

echo Starting Flask server on http://localhost:5000
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python app.py
