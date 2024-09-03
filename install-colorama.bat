@echo off
setlocal

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not added to the PATH.
    echo Please install Python or ensure it is added to your PATH environment variable.
    exit /b %errorlevel%
)

:: Define the package name
set "PACKAGE=colorama"

:: Install the package
echo Installing %PACKAGE% package...
pip install %PACKAGE%
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install %PACKAGE%. Please check your connection or package name.
    exit /b %errorlevel%
)

:: Confirm successful installation
echo.
echo [SUCCESS] %PACKAGE% installed successfully.

:: Clean up
endlocal
pause
