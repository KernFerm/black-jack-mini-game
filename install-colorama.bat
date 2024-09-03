@echo off
setlocal

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
