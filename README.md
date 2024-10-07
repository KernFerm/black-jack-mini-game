<p align="center">
  <img src="https://github.com/KernFerm/black-jack-mini-game/blob/main/Logo/blackjack.png" width="400" alt="Blackjack Logo">
</p>



## READ EVERYTHING CAREFULLY
- **Including**: `Readme.md` , `License` , `Code_of_Conduct.md` , `Security.md`.

- [LICENSE](https://github.com/KernFerm/black-jack-mini-game/blob/main/LICENSE)
- [Code_of_Conduct.md](https://github.com/KernFerm/black-jack-mini-game/blob/main/CODE_OF_CONDUCT.md)
- [Security.md](https://github.com/KernFerm/black-jack-mini-game/blob/main/SECURITY.md)

---
### Support the Project ⭐

- If you find this project useful, please give it a star! Your support is appreciated and helps keep the project growing. 🌟
---

# 🎉 Welcome to Blackjack! 🎉

This is a simple **Blackjack** game written in Python with both **GUI** and **command-line** support. Enjoy the thrill of Blackjack with colorful emojis and a user-friendly graphical interface! 😎🎴

## 🎲 How to Play

1. **Hit 🃏** - Draw another card and add it to your hand.
2. **Stand 🚶** - Keep your current hand and see if you beat the dealer.
3. **Forfeit 🚫** - Give up and let the dealer win automatically.

## 🎨 Features
- **Command-line Version:** Play directly in the terminal using your keyboard.
- **GUI Version:** Play using buttons with a graphical interface (Tkinter-based).
- **🎨 Colored Text:** Uses colorama to bring your game to life with colors!
- **🃏 Card Drawing:** Random card selection simulating a real Blackjack game.
- **🏆 Win Conditions:** Play against the dealer and see if you can beat the house.

The goal is to get as close to 21 as possible without going over. If you go over 21, you **bust** 💥 and lose the game!

### **Download the EXE of the Application [Click Here](https://github.com/KernFerm/black-jack-mini-game/releases/tag/USER-FRIENDLY-EXE)**

- **Follow the Instruction to install `Docker Desktop App` if you need help**
### Join the Discord - [Fnbubbles420 Org Community](https://www.discord.fnbubbles420.org/invite)

-----

# 🃏 Blackjack Game in Docker

This project is a command-line Blackjack game built using Python and Docker.

## Download and install `Docker`
- **[Download Docker](https://desktop.docker.com/win/main/arm64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module)**

## 🐳 Docker Commands

### 🛠️ Build the Docker image:
```
docker build -t blackjack-game .
```
▶️ Run the Docker container interactively:
```
docker run -it blackjack-game
```
♻️ Rebuild the Docker image without cache:
```
docker build --no-cache -t blackjack-game .
```
📋 List running containers:
```
docker ps
```
🛑 Stop a running container:
```
docker stop <container_id>
```
📜 View logs from the container:
```
docker logs <container_id>
```
🗑️ Remove the container:
```
docker rm <container_id>
```
🗑️ Remove the Docker image:
```
docker rmi blackjack-game
```
- These commands will help you manage the Blackjack game using Docker efficiently.


## 🖥 GUI Version

If you prefer a graphical interface, this version comes with a simple Tkinter-based GUI, providing buttons for "Hit," "Stand," and "Forfeit." The game state, including your cards and the dealer's cards, will be displayed in the window.

## 🐍 Python Versions Supported
- This game supports the following Python versions:

1. **Python 3.11.6 - [Download here](https://github.com/KernFerm/Py3.11.6installer)**
2. **Python 3.11.9 - [Download here](https://github.com/KernFerm/Py3.11.9installer)**
3. **Python 3.12.1 - [Download here](https://github.com/KernFerm/Py3.12.1-installer-batch)**

### 🛠 GUI Setup

1. Ensure you have Python installed (3.11.6 or later recommended).
2. Install the required dependencies by running:

    ```
    pip install colorama tk
    ```

3. **Run the game using:**
    ```
    python main.py
    ```


## 🛠 Command-Line Version Setup

### **Option 1: Manual Setup**

1. **Ensure you have Python installed (3.11.6 or later recommended).**
2. **Install the required dependencies by running:**
    ```
    pip install colorama tk
    ```

3. **Download or clone this repo.**
4. **Run the game using:**

    ```
    python main.py
    ```

## **Option 2: Automated Setup Using Batch Script**

- If you prefer an automated setup, you can use the provided batch script:
- A `Batch script` is included in the repo with all the necessary files.
- No need to create a file manually.

## Example Batch Script

```
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
```

- Double-click `install.bat` to run the script. It will automatically install the `colorama` package with a progress bar for better user experience.
- After installation, run the game using:

    ```
    python main.py
    ```

## 📜 License

- This project is proprietary and all rights are reserved by the author. 
Unauthorized copying, distribution, or modification of this project is strictly prohibited. 
Unless You have written permission from the Developer or the FNBUBBLES420 ORG.

## 🎮 Enjoy the Game!

- Have fun playing Blackjack, and may the cards be ever in your favor! 🍀🎴

## Acknowledgement
- Forked repo from [@LeopoldPrime](https://github.com/LeopoldPrime/Blackjack-Minigame) then `Remade it better`.
