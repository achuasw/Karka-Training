quiz=input("Are you ready for a quiz? ")
if quiz=="y":
 print("Okay,here it comes!")
else:
    exit()
    
print("\n")
add=0
capital=int(input("01) What is the capital of Aleska?\n\t1) Melbourne\n\t2) Anchorage\n\t3) Juneas\n"))
if capital==3:
    add=add+1
    print("That's right!")
else:
    print("That's wrong")
print("\n")

store=int(input("02) Can you store the value 'cat' in a variable of type int\n\t1) Yes\n\t2) No\n"))
if store==1:
    print("Sorry,'cat' is a string.ints can only store numbers.")
else:
    add=add+1
    print("That's right")
print("\n")

result=int(input("03) What is the result of 946/3?\n\t1) 5\n\t2) 11\n\t3) 15/3\n"))
if result==2:
    add=add+1
    print("That's correct!")
else:
    print("That's wrong")
print("\n")
print(f"Overall,you got {add} out of 3 correct,\nThanks for playing!")

"""using function
quiz=input("Are you ready for a quiz? ")
print("Okay,here it comes!")
print("\n")
add=0
capital=int(input("01) What is the capital of Aleska?\n\t1) Melbourne\n\t2) Anchorage\n\t3) Juneas\n"))
def simple_quiz(capital,store,result):
    if capital==3:
        add=add+1
        print("That's right!")
    else:
        print("That's wrong")
#print("\n")
    store=int(input("02) Can you store the value 'cat' in a variable of type int\n\t1) Yes\n\t2) No\n"))
    if store==1:
        print("Sorry,'cat' is a string.ints can only store numbers.")
    else:
        add=add+1
    print("That's right")
#print("\n")
    result=int(input("03) What is the result of 946/3?\n\t1) 5\n\t2) 11\n\t3) 15/3\n"))
    if result==2:
        add=add+1
        print("That's correct!")
    else:
        print("That's wrong")
print("\n")
print(f"Overall,you got {add} out of 3 correct,\nThanks for playing!")
"""









