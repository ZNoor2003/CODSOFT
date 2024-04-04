import random

def getUserChoice():
    userChoice = input("Choose ROCK, PAPER OR SCISSORS: ").lower()
    if userChoice == "rock" or userChoice == "paper" or userChoice == "scissors":
        return userChoice
    else:
        print("Invalid Input!. Please enter the correct choice")

def getCompChoice():
    return random.choice(['rock','paper','scissors'])

def getWinner(userChoice, compChoice):
    if userChoice == compChoice:
        return "It's a TIE!!"
    elif (userChoice == 'rock' and compChoice == 'scissors') or \
            (userChoice == 'scissors' and compChoice == 'paper') or \
            (userChoice == 'paper' and compChoice == 'rock'):
        return "You WIN :)"
    else:
        return "You LOSE :("

def playGame():
    userScore = 0
    compScore = 0
    print("---------|ROCK-PAPER-SCISSORS GAME|---------\n")
    while True:
        userChoice  = getUserChoice()
        compChoice = getCompChoice()
        print(f"User's Choice: {userChoice}")
        print(f"Computer's Choice: {compChoice}\n")

        result = getWinner(userChoice, compChoice)
        print(result)

        if "TIE" in result:
            print(f"\n----|Score|----\nYour Score: {userScore}\nComputer's Score: {compScore}")
        elif "WIN" in result:
            userScore += 1
            print(f"\n----|Score|----\nYour Score: {userScore}\nComputer's Score: {compScore}")
        elif "LOSE" in result:
            compScore += 1
            print(f"\n----|Score|----\nYour Score: {userScore}\nComputer's Score: {compScore}")

        INPUT = input("\nDo you want to play again (Y/N): ").lower()
        if INPUT == "n":
            print("Thanks for Playing :)")
            break

playGame()

