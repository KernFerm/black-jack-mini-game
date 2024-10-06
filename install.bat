@echo off
:: Batch script to install colorama and tkinter with a loading bar for finalization

echo Installing colorama...
pip install colorama

echo Press Enter to continue to install the other dependencies.
pause

echo Installing tkinter...
pip install tk

echo Press Enter to finalize the install.
pause

:: Finalization with a loading bar
echo Finalizing...
setlocal
set "progressBar="
for /L %%A in (1,1,10) do (
    set "progressBar=#%progressBar%"
    echo [%progressBar%] %%A0%%
    ping -n 2 127.0.0.1 >nul
)

endlocal
echo All packages have been installed!
echo You may now exit the cmd.exe.
pause
