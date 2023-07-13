gndr=input("What is your gender (M or F): ")
frst_name=input("First_name: ")
lst_name=input("Last_name: ")
age=int(input("Age: "))
sign1="Mrs"
sign2="Miss"
sign3="Mr"
print("\n")
def call_gender():
    if gndr=="female" and age>=20:
        qn1=input(f"Are you married, {frst_name} (yes or no)? ")
        if qn1=="yes":
            print(f"Then I shall call you {sign1},{frst_name}{lst_name}.") 
        elif qn1=="no":
            print(f"Then I shall call you {sign2}, {lst_name}.")             
    elif gndr=="female" and age<20:
        print(f"{frst_name} {lst_name}")
    elif gndr=="male" and age>=20:
        print(f"{sign3} {frst_name} {lst_name}")
    else:
            print(f"{frst_name} {lst_name}")   
# qn1=input(f"Are you married, {frst_name} (yes or no)? ")     
call_gender() 
       

  


    
