import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def play_round():
    print("\nChoose rock, paper, or scissors:")
    user_choice = input().lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return None, None
    
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("You lose!")
    
    return winner, computer_choice

def main():
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        winner, computer_choice = play_round()
        if winner is None:
            continue
        
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer")
        
        print("Do you want to play another round? (yes or no)")
        play_again = input().lower()
        if play_again != 'yes':
            break
    
    print("Thanks for playing!")
    print(f"Final Score: You {user_score} - {computer_score} Computer")

if __name__ == "__main__":
    main()
