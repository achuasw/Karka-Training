name=input("Hey,what's your name? (Sorry,I keep forgetting.)")
age=int(input(f"Ok,{name},how old are you? "))
if age<16:
    print("you can't drive.")
elif age==16 or age==17:
    print("You can drive but not vote.")
elif age>=18 and age<=24:
    print("You can vote but not rent a car.")
elif age>=25:
     print("You can do pretty much anything.")
else:
    print("number not defined")

#using function
name=input("Hey,what's your name? (Sorry,I keep forgetting.)")
#age=int(input(f"Ok,{name},how old are you? "))
def message(age):
    if age<16:
        return("you can't drive.")
    elif age==16 or age==17:
        return("You can drive but not vote.")
    elif age>=18 and age<=24:
        return("You can vote but not rent a car.")
    elif age>=25:
         return("You can do pretty much anything.")
    else:
        return("number not defined")

age=int(input(f"Ok,{name},how old are you?  "))
old=message(age)
print(old)
