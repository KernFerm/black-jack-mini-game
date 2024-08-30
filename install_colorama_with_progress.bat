@echo off
:: Batch script to install colorama with a progress bar

:: Function to display progress bar
:ProgressBar
setlocal
set "progressBar="
set /A "percentage=(%1*10)/100"
for /L %%A in (1, 1, 10) do (
    if %%A leq %percentage% (
        set "progressBar=#%progressBar%"
    ) else (
        set "progressBar= %progressBar%"
    )
)
set "bar=[%progressBar%] %1%%"
echo %bar%
endlocal & set "progressBar=%bar%"
goto :eof

:: Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Python is not installed. Please install Python before running this script.
    pause
    exit /b 1
)

:: Install colorama using pip
echo Installing colorama package...
for %%i in (10 20 30 40 50 60 70 80 90 100) do (
    ping -n 2 127.0.0.1 >nul
    call :ProgressBar %%i
)

pip install colorama >nul 2>&1

:: Check if installation was successful
pip show colorama >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Failed to install colorama. Please try installing it manually.
    pause
    exit /b 1
)

echo.
echo Colorama has been successfully installed!
pause
