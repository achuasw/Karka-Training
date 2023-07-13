name=input("What's is your name? ")
age=int(input(f"\nOk,{name}, how old are you? "))
print("\n")
if age<16:
    print(f"You can't drive,{name}")
elif age<18:
    print(f"You can't vote,{name}")
elif age<25:
    print(f"You can't rent a car,{name}")
elif age>=25:
    print(f"You can do anything that's legal,{name}")
else:
    print(f"\nYou can't vote,{name},\nYou can't rent a car.{name}.")