current_earth_weight=float(input("Please enter your current earth weight: "))
print("\n")
planet1="venus"
planet2="mars"
planet3="jupiter"
planet4="saturn"
planet5="uranus"
planet6="neptune"
weight=0
print(f"I have information for the following planets:\n\t1. {planet1}  2. {planet2}   3. {planet3}\n\t4. {planet4} 5. {planet5} 6. {planet6}")
visit=int(input("Which planet are you visiting? "))
if visit==1:
    gravity1=0.78
    weight=float(current_earth_weight*gravity1)
    print(weight)
elif visit==2:
    gravity2=0.39
    weight=float(current_earth_weight*gravity2)
    print(weight)    
elif visit==3:
    gravity3=2.65
    weight=float(current_earth_weight*gravity3)
    print(weight)
elif visit==4:
    gravity4=1.17
    weight=float(current_earth_weight*gravity4)
    print(weight)
elif visit==5:
    gravity5=1.05
    weight=float(current_earth_weight*gravity5)
    print(weight)
elif visit==6:
    gravity6=1.23
    weight=float(current_earth_weight*gravity6)
    print(weight)
else:
    print("undefined planet")
print(f"your weight would be {weight} pounds on that planet.") 