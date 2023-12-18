import random

def coin_toss():
    return random.choice(['Heads', 'Tails'])

def play_two_up():
    input("Press Enter to toss the coins...")
    coin_01 = coin_toss()
    coin_02 = coin_toss()
    
    print(f"Coin 1: {coin_01}")
    print(f"Coin 2: {coin_02}")
    
    if coin_01 == coin_02:
        print("You win!")
    else:
        print("You lose!")

# Main game loop
while True:
    print("\n=== Welcome to Two-Up! ===")
    print("Try your luck by tossing two coins.")
    play_two_up()

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thank you for playing Two-Up!")
        break