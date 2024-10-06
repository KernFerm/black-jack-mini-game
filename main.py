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

# 🎴 Cards available to be selected (simplified to only face values including Ace)
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # 10 repeated to simulate face cards

# 🎲 Function to draw a card
def draw_card():
    return random.choice(cards)

# 🎴 Function to calculate the total of a hand with Ace handling
def calculate_total(cards):
    total = sum(cards)
    # If there's an Ace and it can count as 11 without busting, count it as 11
    if 1 in cards and total + 10 <= 21:
        return total + 10
    return total

# 💡 Function to check if the player has busted
def check_bust(cards):
    return calculate_total(cards) > 21

# 🤵 Dealer's turn logic: Dealer hits until they reach 17 or more
def dealer_turn(dealer_cards):
    while calculate_total(dealer_cards) < 17:
        new_card = draw_card()
        dealer_cards.append(new_card)
        print(Fore.YELLOW + f"🤵 Dealer draws a {new_card}. Dealer's cards: {', '.join(map(str, dealer_cards))}")
        time.sleep(1)
    return dealer_cards

# 🎴 Drawing the initial cards for the player and the dealer
player_cards = [draw_card(), draw_card()]
dealer_cards = [draw_card(), draw_card()]

# 🃏 Displaying the initial cards with color
print(f"{Fore.YELLOW}🤵 Dealer's cards: {dealer_cards[0]} 🂠")
time.sleep(1)
print(f"{Fore.CYAN}🃏 Your cards: {player_cards[0]} and {player_cards[1]}")
time.sleep(1)

# 📊 Game loop for player decisions
while True:
    # Clear the screen for better readability
    clear_screen()

    # Display current hands
    print(f"{Fore.YELLOW}🤵 Dealer's cards: {dealer_cards[0]} 🂠")
    print(f"{Fore.CYAN}🃏 Your cards: {', '.join(map(str, player_cards))} (Total: {calculate_total(player_cards)})")

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
        # Player stands, it's the dealer's turn
        dealer_cards = dealer_turn(dealer_cards)
        print(Fore.YELLOW + f"\n🤵 Dealer's final cards: {', '.join(map(str, dealer_cards))} (Total: {calculate_total(dealer_cards)})")
        time.sleep(1)
        print(Fore.CYAN + f"🃏 Your final cards: {', '.join(map(str, player_cards))} (Total: {calculate_total(player_cards)})")
        time.sleep(1)

        # Compare hands to determine the winner
        if check_bust(dealer_cards):
            print(Fore.GREEN + "🎉 Dealer busted! You win! 🎉")
        elif calculate_total(player_cards) > calculate_total(dealer_cards):
            print(Fore.GREEN + "🎉 You have won! Congratulations! 🎉")
        elif calculate_total(player_cards) == calculate_total(dealer_cards):
            print(Fore.YELLOW + "🤝 It's a tie!")
        else:
            print(Fore.RED + "😢 You have lost. Better luck next time! 😢")
        sys.exit()
    elif player_input == '3':
        # Player forfeits
        print(Fore.RED + "🚫 You forfeited. The dealer wins automatically.")
        sys.exit()
    else:
        print(Fore.RED + "❗ Invalid input. Please enter 1, 2, or 3.")

    # Check if the player has 5 cards without busting (automatic win)
    if len(player_cards) == 5 and not check_bust(player_cards):
        print(Fore.GREEN + "🎉 You have 5 cards without busting! You automatically win! 🎉")
        sys.exit()
