print("OLD KEYCHAIN SHOP\n")

#cost=10
#no=0
#tax=0.0825
#shipping_cost=5.00
#additional=1.00

def add_keychains(no):
    add=int(input(f"\nYou have {no} keychains. How many to add? "))
    keychain=no+add
    print(f"You now have {keychain} keychains.")
    return keychain
#add=add_keychains(0)

def remove_keychains(sub):
    minus=int(input(f"\nYou have {add} keychains. How many to remove? "))
    remove=sub-minus
    print(f"You now have {remove} keychains.") 
    return remove
#total=remove_keychains(add)
def view_order(sub,tax,shipping_cost,cost,additional):
    total_cost=sub*cost
    charge=shipping_cost+additional
    order=tax*sub
    final_cost=order+total_cost
    #print(f"You have {sub} keychains.\nkeychains cost ${cost} each.\nThe shipping charges on the order ${charge}.\nThe sub total before ${total_cost}.\nThe tax on the order {order}.\nThe final cost of the order {final_cost}")
    return final_cost
#cart=view_order(total,0.0825,5.00,10,1.00)
def checkout(sub,cost,charge,total_cost,order,):
    
    print("\nCHECKOUT\n")
    name=input("What is your name? ")
    print("Please check your order!")
    print(f"You have {sub} keychains.\nkeychains cost ${cost} each.\nThe shipping charges on the order ${charge}.\nThe sub total before ${total_cost}.\nThe tax on the order {order}.\nThe final cost of the order {cart}")
    view_order(total,0.0825,5.00,10,1.00)
    print(f"\nThanks for your order, {name} ")
    exit()
while True:
        print("\n1. Add keychains to order\n2. Remove keychains from order\n3. View current order\n4. Checkout")  
        choice=int(input("Please enter the choice: ")) 
        if choice==1:
            add=add_keychains(0)
        elif choice==2:
            total=remove_keychains(add)
        elif choice==3:
            order=view_order(total,0.0825,5.00,10,1.00)
        elif choice==4:
            checkout()
        else:
            print("Wrong choice") 
            break
                