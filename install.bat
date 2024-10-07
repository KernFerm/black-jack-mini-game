@echo off
:: Install required packages

pip install setuptools>=75.1.0 colorama>=0.4.5 tk

:: Loading bar
echo Finalizing installation...
setlocal
set "progressBar="
for /L %%A in (1,1,10) do (
    set "progressBar=#%progressBar%"
    echo [%progressBar%] %%A0%%
    ping -n 2 127.0.0.1 >nul
)

endlocal
echo Installation complete!
pause
