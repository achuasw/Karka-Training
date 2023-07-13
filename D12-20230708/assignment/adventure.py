print("WELCOME TO ACHU'S TINY ADVENTURE!\n")
room1=input("You are in a creepy house! Would you like to go 'upstairs' or into the 'kitchen'?\n")
def creepy_house():
    if room1=="kitchen" or room1=="upstairs":
        print("\n")
        room2=input("There is a long countertop with dirty dishes everywhere, Off to one side\nthere is. as you'd expect, a refrigerator, You say open the 'refrigerator'\nor look in a 'cabinet'.\n")
        if room2=="refrigerator":
            print("\n")
            inside=input(f"Inside the {room2} you see food and stuff. It looks pretty nasty.\nWould you like to eat some of the food? ('yes' or 'no')\n ")
            if inside=="no":
                print("\n")
                print("You die of starvation...eventually.")
            elif inside=="yes":
                print("\n")    
                print("I will be alive")
        elif room2=="cabinet":
            print("\n")
            room3=input("A cabinet that has a book is locked ('open' or 'close')\n")
            if room3=="open":
                print("\n")
                print("I can read the book")
            elif room3=="close":    
                print("\n")
                print("I can't read the book")
        elif room2=="nothing":
            print("\n")
            room3=input("oh no, nothing is there I want to go to the next room ('go' or 'not')")
            if room3=="go":
                print("\n")
                print("oh I came again to the kitchen")
            elif room3=="not":
                print("\n")
                print("BOOORING....!")
            else:
                print("\n")
                print("GAME OVER!")    

creepy_house()


