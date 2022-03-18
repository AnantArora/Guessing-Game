import random 

GuessingNumber= random.randint(0,9)

chance = 0
while (chance < 6):
    introString = int(input("type a number between 1 to 9: "))
    if (introString > GuessingNumber):
        print("Your guess is large")
    elif (introString == GuessingNumber):
        print("Congratulations! You guessed is correct 🙌 🎉")
    else :
        print("Your number guess is less")
    chance = chance + 1
if (chance > 6):
    print("You lose 😢")


