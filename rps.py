import random

score_player = 0
score_computer = 0

def scpl():
    global score_player
    score_player += 1

def sccp():
    global score_computer
    score_computer += 1

def scz(score_player = 0, score_computer = 0):
    return
    

def get_user_choice():
    user_choice = input("chooce your destiny ").lower()
    while user_choice not in ['rock', 'paper', 'scizors', "geko", "spok"]:
        print("eror name")
        user_choice = input("again ").lower()
    return user_choice


def get_computer_choice():
    return random.choice(["rock", "paper", "scizors", "geko", "spok"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif ((user_choice == "rock" and computer_choice == "scizors") 
          or (user_choice == "scizors" and computer_choice == "paper") 
          or (user_choice == "paper" and computer_choice == "rock") 
          or (user_choice == "rock" and computer_choice == "geko") 
          or (user_choice == "geko" and computer_choice == "spok") 
          or (user_choice == "spok" and computer_choice == "scizors") 
          or (user_choice == "scizors" and computer_choice == "geko") 
          or (user_choice == "geko" and computer_choice == "paper") 
          or (user_choice == "paper" and computer_choice == "spok") 
          or (user_choice == "spok" and computer_choice == "rock")):
        scpl()
        return f"you win"
    else:
        sccp()
        return f"you lose"
        



def game():
    print("buongiorno")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"your choice: {user_choice}")
        print(f"computer choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)
        print(score_player, score_computer)

        if score_player == 3 or score_computer == 3:
            play_again = input("play again (Y|N)").lower()
            if play_again == 'N' or play_again == "n":
                print("thanks. goodbye")
                break
            else:
              game() and scz()
        else:
            game()

game()