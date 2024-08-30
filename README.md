# 🎉 Welcome to Blackjack! 🎉

This is a simple command-line Blackjack game written in Python. Enjoy the thrill of Blackjack with just a few lines of code and some colorful emojis! 😎🎴

## 🎲 How to Play

1. **Hit 🃏** - Draw another card and add it to your hand.
2. **Stand 🚶** - Keep your current hand and see if you beat the dealer.
3. **Forfeit 🚫** - Give up and let the dealer win automatically.

The goal is to get as close to 21 as possible without going over. If you go over 21, you **bust** 💥 and lose the game!

### If you dont have a pet python here is a couple below:
- **YOU ONLY NEED ONLY VERSION OF PYTHON TO RUN THIS !!**
- [Python 3.11.6](https://github.com/KernFerm/Py3.11.6installer)
- [Python 3.11.9](https://github.com/KernFerm/Py3.11.9installer)
- [Python 3.12.1](https://github.com/KernFerm/Py3.12.1-installer-batch)

### 📝 User Commands

- `1` 👉 **Hit** - Draw a card.
- `2` 👉 **Stand** - End your turn and let the dealer play.
- `3` 👉 **Forfeit** - Give up the game.

## 🛠 Installation & Setup

### Option 1: Manual Setup

1. Ensure you have Python installed (3.6 or later recommended).
2. Install the required dependencies by running:

   ```
   pip install colorama
   ```
3. Download or clone this repository.
4. Run the game using:
   ```
   python main.py
   ```
## Option 2: Automated Setup Using Batch Script
- If you prefer an automated setup, you can use the provided batch script:
- `Batch script` is included in the repo above with all the rest of the files
- `So no need to create a file.`

### example 
```batch
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
```
- Double-click `install_colorama.bat` to run the script. It will automatically install the `colorama` package with a progress bar for better user experience.

- After installation, run the game using:
  ```
  python main.py
  ```

## 🚀 Features

- 🎨 Colored Text: Uses `colorama` to bring your game to life with colors!
- 🃏 Card Drawing: Random card selection simulating a real Blackjack game.
- 🥇 Win Conditions: Play against the dealer and see if you can beat the house.

## 👨‍💻 Contributing
- Feel free to fork this repository and make improvements. Contributions are welcome! 🛠✨

## 📜 License
- This project is licensed under the [MIT License](https://github.com/KernFerm/black-jack-mini-game/blob/main/LICENSE). See the LICENSE file for details.


# 🎮 Enjoy the Game!
- **Have fun playing Blackjack, and may the cards be ever in your favor! 🍀🎴**

------
------

