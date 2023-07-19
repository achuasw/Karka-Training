import random
def hilo():
    chance=0
    #number=random.randint(1,100)
    while chance<7:
        chance+=1
        number=random.randint(1,100)
        quest=input("First guess: ")
        if quest==number:
            print("You guessed it! What are the odds?!?")
        elif quest!=number:
            print("Sorry, you are too low.")
hilo()

