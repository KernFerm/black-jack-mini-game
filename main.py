import random
import time
import os
import sys
from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# 🎉 Welcome message with an emoji and colored text
clear_screen()
print(Fore.GREEN + "🎉 Welcome to Blackjack! 🎉")

# 🎴 Cards available to be selected (simplified to only face values)
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 🎲 Function to draw a card
def draw_card():
    return random.choice(cards)

# 🎴 Drawing the initial cards for the player and the dealer
player_cards = [draw_card(), draw_card()]
dealer_cards = [draw_card(), draw_card()]

# 🃏 Displaying the initial cards with color
print(f"{Fore.YELLOW}🤵 Dealer's cards: {dealer_cards[0]} 🂠")
time.sleep(1)
print(f"{Fore.CYAN}🃏 Your cards: {player_cards[0]} and {player_cards[1]}")
time.sleep(1)

# 🔄 Function to calculate the total of a hand
def calculate_total(cards):
    return sum(cards)

# 💡 Function to check if the player has busted
def check_bust(cards):
    return calculate_total(cards) > 21

# 📊 Game loop for player decisions
while True:
    # Clear the screen for better readability
    clear_screen()

    # 📝 Asking the player for their decision
    print("\n" + Fore.MAGENTA + "What would you like to do? 🤔")
    print(Fore.BLUE + "👉 (1) Hit 🃏")
    print(Fore.YELLOW + "👉 (2) Stand 🚶")
    print(Fore.RED + "👉 (3) Forfeit 🚫")
    player_input = input(Fore.WHITE + "Enter the number of your choice: ")

    if player_input == '1':
        # Player hits
        new_card = draw_card()
        player_cards.append(new_card)
        print(Fore.CYAN + f"🃏 You drew a {new_card}. Your cards are now: {', '.join(map(str, player_cards))}")
        time.sleep(1)
        if check_bust(player_cards):
            print(Fore.RED + "💥 You've gone above 21! You busted! 💥")
            sys.exit()
    elif player_input == '2':
        # Player stands
        print(Fore.YELLOW + f"\n🤵 Dealer's cards: {dealer_cards[0]} and {dealer_cards[1]}")
        time.sleep(1)
        print(Fore.CYAN + f"🃏 Your cards: {', '.join(map(str, player_cards))}")
        time.sleep(1)
        if calculate_total(player_cards) >= calculate_total(dealer_cards):
            print(Fore.GREEN + "🎉 You have won! Congratulations! 🎉")
        else:
            print(Fore.RED + "😢 You have lost. Better luck next time! 😢")
        sys.exit()
    elif player_input == '3':
        # Player forfeits
        print(Fore.YELLOW + f"🤵 Dealer's cards: {dealer_cards[0]} and {dealer_cards[1]}")
        time.sleep(1)
        print(Fore.CYAN + f"🃏 Your cards: {', '.join(map(str, player_cards))}")
        time.sleep(1)
        print(Fore.RED + "🚫 You forfeited. The dealer wins automatically.")
        sys.exit()
    else:
        print(Fore.RED + "❗ Invalid input. Please enter 1, 2, or 3.")

    # Check if the player has 5 cards without busting (automatic win)
    if len(player_cards) == 5 and not check_bust(player_cards):
        print(Fore.GREEN + "🎉 You have 5 cards without busting! You automatically win! 🎉")
        sys.exit()
