@echo off
:: Batch script to install colorama, setuptools, and tkinter with a loading bar for finalization

echo Installing setuptools...
pip install setuptools>=75.1.0

echo Press Enter to continue to install the other dependencies.
pause

echo Installing colorama...
pip install colorama>=0.4.5

echo Press Enter to continue to install tkinter.
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
