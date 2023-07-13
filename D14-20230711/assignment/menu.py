def add_keychains():
    print("\nADD KEYCHAINS")
def remove_keychains():
    print("\nREMOVE KEYCHAINS")
def view_order():
    print("\nVIEW ORDER")
def checkout():
    print("\nCHECKOUT")
print("OLD KEYCHAIN SHOP\n\n1. Add keychains to order\n2. Remove keychains from order\n3. View current order\n4. Checkout")

#choice=int(input("Enter your choice: "))
"""while choice<4:
   choice=choice+0
   print("\n1. Add keychains to order\n2. Remove keychains from order\n3. View current order\n4. Checkout")
   break"""


while True:
   choice=int(input("Please enter your choice: "))
   if choice==1:
     add_keychains()
   elif choice==2:
     remove_keychains()
   elif choice==3:
     view_order()
   elif choice==4:
      checkout()
      exit()
   print("\n1. Add keychains to order\n2. Remove keychains from order\n3. View current order\n4. Checkout")
   break
