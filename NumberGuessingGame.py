import random as r

# This will be a number guessing game

# Create a game loop
exit = False
while exit == False:
    
    print("System has picked a number between 1 and 100, lets start!")
    randomNumber = r.randint(1,100)
    gameCount = 0
    userNumber = 0
    
    while userNumber != randomNumber:
        try:
            userNumber = int(input("Please enter a number: "))
        except Exception as e:
            print(f"Error, please use a number only! Defaulting guess to 0!")

        if userNumber > randomNumber:
            print(f"{userNumber} is higher!")
        elif userNumber < randomNumber:
            print(f"{userNumber} is lower!")
        gameCount += 1   
    
    # Option to exit the game
    userOption = input(f"You've guessed {randomNumber} in {gameCount} turns! Do you still want to play? Y/N: ")
    if userOption.upper() == "N":
        exit = True