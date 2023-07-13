print("OLD KEYCHAIN SHOP\n")

cost=10
no=0

def add_keychains(no):
    add=int(input(f"\nYou have {no} keychains. How many to add? "))
    keychain=no+add
    print(f"You now have {keychain} keychains.")
    return keychain
#tot=add_keychains(no)
def remove_keychains(keychain):
    minus=int(input(f"\nYou have {keychain} keychains. How many to remove? "))
    sub=keychain-minus
    print(f"You now have {sub} keychains.") 
    return sub
#remove=remove_keychains(tot)
def view_order(sub):
    total_cost=sub*cost
    print(f"You have {sub} keychains.\nkeychains cost ${cost} each.\nTotal cost is ${total_cost}.")
    return total_cost
#order=view_order(remove)
def checkout(sub,total_cost):
    print("\nCHECKOUT\n")
    name=input("What is your name? ")
    print(f"You have {sub} keychains.\nkeychains cost ${cost} each.\nTotal cost is ${total_cost}.\nThanks for your order, {name} ")
    exit()
while True:
        print("\n1. Add keychains to order\n2. Remove keychains from order\n3. View current order\n4. Checkout")  
        choice=int(input("Please enter the choice: ")) 
        if choice==1:
            tot=add_keychains(no)
        elif choice==2:
            remove=remove_keychains(tot)
        elif choice==3:
            order=view_order(remove)
        elif choice==4:
            checkout(remove,order)
        else:
            print("Wrong choice")
            break
