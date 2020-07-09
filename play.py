import random
print("According to Sheldon, the winning rules of the Rock Paper Scissors Lizard Spock game are as follows: \n"
    + "Scissors cuts Paper \n"
    + "Paper covers Rock \n"
    + "Rock crushes Lizard \n"
    + "Lizard poisons Spock \n"
    + "Spock smashes Scissors \n"
    + "Scissors decapitates Lizard \n"
    + "Lizard eats Paper \n" 
    + "Paper disproves Spock \n"
    + "Spock vaporizes Rock \n"
    + "and as it always has, Rock crushes Scissors \n")

win_clause = "You win! "
lose_clause = "You lose! "

scissors_paper_clause = "Scissors cuts Paper!"
papar_rock_clause = "Paper covers Rock!"
rock_lizard_clause = "Rock crushes Lizard!"
lizard_spock_clause = "Lizard poisons Spock!"
spock_scissors_clause = "Spock smashes Scissors!"
scissors_lizard_clause = "Scissors decapitates Lizard!"
lizard_paper_clause = "Lizard eats Paper!"
paper_spock_clause = "Paper disproves Spock!"
spock_rock_clause = "Spock vaporizes Rock!"
rock_scissors_clause = "Rock crushes Scissors!"

while True: 
    print("Please Enter your choice: \n 1. Rock \n 2. Paper \n 3. Scissors \n 4. Lizard \n 5. Spock \n")
    user_choice = int(input("Your turn: "))
    while not isinstance(user_choice, int) or user_choice < 1 or user_choice > 5: 
        user_choice = int(input("Ooops! Please enter a valid input! Your turn: "))
    if user_choice == 1:
        user_choice_name = "Rock"
    elif user_choice == 2:
        user_choice_name = "Paper"
    elif user_choice == 3: 
        user_choice_name = "Scissors"
    elif user_choice == 4: 
        user_choice_name = "Lizard"
    else: 
        user_choice_name = "Spock"
    
    print("Your choice is " + user_choice_name)
    print("Now it is computer's turn! ") 

    computer_choice = random.randint(1, 5)
    if computer_choice == 1: 
        computer_choice_name = "Rock"
    elif computer_choice == 2:
        computer_choice_name = "Paper"
    elif computer_choice == 3: 
        computer_choice_name = "Scissors"
    elif computer_choice == 4:
        computer_choice_name = "Lizard"
    else:
        computer_choice_name = "Spock"
    
    print("The computer's choice is " + computer_choice_name)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 1 and computer_choice == 2:
        print(lose_clause + papar_rock_clause) 
    elif user_choice == 1 and computer_choice == 3: 
        print(win_clause + rock_scissors_clause)
    elif user_choice == 1 and computer_choice == 4:
        print(win_clause + rock_lizard_clause)
    elif user_choice == 1 and computer_choice == 5: 
        print(lose_clause + spock_rock_clause)
    elif user_choice == 2 and computer_choice == 1: 
        print(win_clause + papar_rock_clause)
    elif user_choice == 2 and computer_choice == 3: 
        print(lose_clause + scissors_paper_clause)
    elif user_choice == 2 and computer_choice == 4: 
        print(lose_clause + lizard_paper_clause)
    elif user_choice == 2 and computer_choice == 5:
        print(win_clause + paper_spock_clause)
    elif user_choice == 3 and computer_choice == 1: 
        print(lose_clause + rock_scissors_clause)
    elif user_choice == 3 and computer_choice == 2:
        print(win_clause + scissors_paper_clause)
    elif user_choice == 3 and computer_choice == 4:
        print(win_clause + scissors_lizard_clause)
    elif user_choice == 3 and computer_choice == 5: 
        print(lose_clause + spock_scissors_clause)
    elif user_choice == 4 and computer_choice == 1: 
        print(lose_clause + rock_lizard_clause)
    elif user_choice == 4 and computer_choice == 2:
        print(win_clause + lizard_paper_clause)
    elif user_choice == 4 and computer_choice == 3:
        print(lose_clause + scissors_lizard_clause)
    elif user_choice == 4 and computer_choice == 5:
        print(win_clause + lizard_spock_clause)
    elif user_choice == 5 and computer_choice == 1:
        print(win_clause + spock_rock_clause)
    elif user_choice == 5 and computer_choice == 2: 
        print(lose_clause + paper_spock_clause)
    elif user_choice == 5 and computer_choice == 3:
        print(win_clause + spock_scissors_clause)
    else: 
        print(lose_clause + lizard_spock_clause)
    
    print("Do you want to play again? (Y/N)")
    user_input = raw_input()
    if user_input == "N" or user_input == "n":
        break