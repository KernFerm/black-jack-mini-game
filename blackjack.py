import random
import time
import os
from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# 🎉 Welcome message with an emoji and colored text
def print_welcome_message():
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
    if 1 in cards and total + 10 <= 21:  # If Ace exists and can count as 11
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

# 🎴 Initialize game state variables
def initialize_game():
    global player_cards, dealer_cards, game_active
    player_cards = [draw_card(), draw_card()]
    dealer_cards = [draw_card(), draw_card()]
    game_active = True  # Track if the game is still ongoing

# 🃏 Display the current game state
def print_game_state():
    clear_screen()
    print(Fore.YELLOW + f"🤵 Dealer's cards: {dealer_cards[0]} 🂠")
    print(Fore.CYAN + f"🃏 Your cards: {', '.join(map(str, player_cards))} (Total: {calculate_total(player_cards)})")

# 🃏 Handle the player "Hit"
def hit():
    global game_active
    if not game_active:
        return  # Don't allow hits if the game is over
    new_card = draw_card()
    player_cards.append(new_card)
    print(Fore.CYAN + f"🃏 You drew a {new_card}. Your cards: {', '.join(map(str, player_cards))}")
    if check_bust(player_cards):
        print(Fore.RED + "💥 You've gone above 21! You busted! 💥")
        end_game()
    print_game_state()

# 🤵 Handle the player "Stand" (dealer plays)
def stand():
    global game_active
    if not game_active:
        return  # Don't allow standing if the game is over
    dealer_cards_final = dealer_turn(dealer_cards)
    print(Fore.YELLOW + f"\n🤵 Dealer's final cards: {', '.join(map(str, dealer_cards_final))} (Total: {calculate_total(dealer_cards_final)})")
    print(Fore.CYAN + f"🃏 Your final cards: {', '.join(map(str, player_cards))} (Total: {calculate_total(player_cards)})")

    if check_bust(dealer_cards_final):
        print(Fore.GREEN + "🎉 Dealer busted! You win! 🎉")
    elif calculate_total(player_cards) > calculate_total(dealer_cards_final):
        print(Fore.GREEN + "🎉 You have won! Congratulations! 🎉")
    elif calculate_total(player_cards) == calculate_total(dealer_cards_final):
        print(Fore.YELLOW + "🤝 It's a tie!")
    else:
        print(Fore.RED + "😢 You have lost. Better luck next time! 😢")
    end_game()

# 🚫 Handle the player "Forfeit"
def forfeit():
    global game_active
    if not game_active:
        return  # Don't allow forfeiting if the game is over
    print(Fore.RED + "🚫 You forfeited. The dealer wins automatically.")
    end_game()

# 🔄 End the game
def end_game():
    global game_active
    game_active = False
    print(Fore.MAGENTA + "🔄 The game has ended. Start a new game by pressing 'New Game'.")

# 🔄 Handle "New Game"
def new_game():
    initialize_game()  # Reset the game state
    print_welcome_message()
    print_game_state()

# 🎴 Start the game
initialize_game()
print_welcome_message()
print_game_state()

# Main game loop
while True:
    while game_active:
        action = input("Choose: [H]it, [S]tand, [F]orfeit, [Q]uit: ").lower()
        if action == 'h':
            hit()
        elif action == 's':
            stand()
        elif action == 'f':
            forfeit()
        elif action == 'q':
            print("Thanks for playing!")
            exit()  # Exit the program if the player chooses to quit
        else:
            print("Invalid input!")

    # After the game ends, ask if the user wants to play again
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == 'y':
        new_game()
    elif play_again == 'q':
        print("Thanks for playing!")
        break
    else:
        print("Thanks for playing!")
        break