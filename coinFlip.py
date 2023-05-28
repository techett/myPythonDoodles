'''

Coin flip

Rules:
1. You will enter /flip to flip your coin
2. You start with a balance of 5 and must have at least five balance to continue playing; however,
if you run out of balance or are below the 5 minimum balance every 300 seconds you will get an addition 5 balance.
3. If you make it to balance 1,000 you win.
4. Max flips are 50 balance

'''

import random  # Imported for random choice
import time  # For tracking time before replenishment
import threading

# Debugging
logging = True

# Misc settings
game_on = True
winning_balance = 1000

# Predetermined win/loss number
coin_sides = ["heads", "tails"]

# Staring balance of player
balance = 5
minimum_balance = 5
balance_refresh_rate = 300
max_wager = 50

# Replenishment ##############################################


def replenishment():  # Handling replenishment
    # Starting off with the timer, before firing off.
    time.sleep(balance_refresh_rate)
    while True:
        if balance < minimum_balance:
            balance += 5
            print(f"Balance replenished. Your new balance is {balance}")
        else:
            if logging:
                print(
                    f"Your balance remained the same. Your current balance is: {balance}")
            time.sleep(balance_refresh_rate)


##############################################################

def play_again():
    while True:
        try:
            play_again_prompt = input("Would you like to play again?\n")

            if play_again_prompt.islower == "yes" or play_again_prompt.islower == "y":
                balance = 5
                main()
            elif play_again_prompt.islower == "no" or play_again_prompt.islower == "n":
                print("Thank you for playing!")
                exit()
            else:
                print("Please enter yes or no.")

        except ValueError:
            print("Invalid input. Try again.")


def check_wager(wager):

    if wager > balance:
        print(
            f"You don't have enough balance for this wager. Your balance is: {balance}")
        coin_flip()

    if wager < minimum_balance:
        print(
            f"This wager does not meet the requirements. Minimum wagers are: {minimum_balance}")
        coin_flip()

    if wager > max_wager:
        print(
            f"This wager does not meet the requirements. Maximum wagers are: {max_wager}")
        coin_flip()


def coin_flip():

    if balance >= winning_balance:
        print(f"You won the game! Your balance is: {balance}\n")
        play_again()

    if balance < minimum_balance:
        print("You don't have enough balance to wager yet. Please wait.")
        time.sleep(balance_refresh_rate)
        coin_flip()
    else:
        while True:
            try:
                wager = int(input("What is your wager?\n"))
                break
            except ValueError:
                print("Please make sure to use numbers only.")

        check_wager(wager)

        outcome = random.choice(coin_sides)

        if outcome == coin_sides[1]:
            balance -= wager
            print(f"You lost! Your new balance is: {balance}")
            coin_flip()
        else:
            balance += wager
            print(f"You won! Your new balance is: {balance}")
            coin_flip()


def main():
    while game_on:
        # Thread it so it can run in the background
        replenishment_thread = threading.Thread(target=replenishment)
        replenishment_thread.start()  # Start the thread

        # Welcome message
        print(
            f"Welcome to Coin Flip Simulator. Your balance is {balance}.\n")
        print("Rules are simple...\nYou must flip your coin and if you lose you'll be deducted balance and if you win you'll be added balance.")
        print("Max flips are 50 balance.\nMinimum flips are 5 balance.\n")
        print("If you drop below 5, don't worry you'll be replenished balance every 5 minutes.\n")
        print("To flip you will need to enter your wager.")
        print("If you win, you'll get the original 10 + 10 to your balance.\n")
        print("The objective is to reach a balance of 1,000. If you can do this, you will win.\n")

        # Start of game functions
        coin_flip()


main()
