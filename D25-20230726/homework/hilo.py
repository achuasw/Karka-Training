import random
number=random.randint(1,100)
chance=0
while chance<7:
    chance=chance+1
    guess=int(input(f"guess {chance}:"))
    if guess<number:
        print("sorry,you are too low.")
    elif guess>number:
        print("sorry,you are too high.")
    else:
        print("you guess it!")
        exit()
print("Sorry you did'nt guess it in seven tries, YOU LOSE.")