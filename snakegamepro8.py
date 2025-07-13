import random

print("Snake Water Gun Game! (s = Snake, w = Water, g = Gun)")

userstore = { "s":"Snake", "w":"Water", "g": "Gun" }

while True:
    choice = ["s", "w", "g"]
    computer = random.choice(choice)

    userinput = input("Choose one [s / w / g] or 'q' to quit: ").lower()

    if userinput == 'q':
        print("Thanks for playing!")
        break

    if userinput not in choice:
        print("Invalid input! Please select s, w, or g.")
        continue

    print(f"You chose: {userstore[userinput]}")
    print(f"Computer chose: {userstore[computer]}")

    # Game rules
    if computer == userinput:
        print("It's a draw!\n")
    elif (userinput == "s" and computer == "w") or \
         (userinput == "w" and computer == "g") or \
         (userinput == "g" and computer == "s"):
        print("You win!\n")
    else:
        print("You lose!\n")
        print ("  <@>  GAME OVER <@>    ")
        
