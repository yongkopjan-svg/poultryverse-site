@echo off
rem Double-click me to start the farm console.
cd /d "%~dp0"
start "farm server" /min pythonw server.py
timeout /t 1 /nobreak >nul
start "" http://localhost:8621
