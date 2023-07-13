def bmi_calculator(weight,tall): 
  BMI=weight/(tall*tall)
  return BMI

#height=float(input("Your height in m: "))
#weight=int(input("Your weight in kg: "))  
#check=bmi_calculator(73,1.75)  
#print(check)

"""category1="under weight"
category2="normal weight"
category3="over weight"
category4="obese"
#def check1(a):
 #   c=a+1
  #  return c
def bmi_calc(weight,height):
#bmi=weight/(height*height)
   # height=float(input("Your height in m: "))
    #weight=float(input("Your weight in KG: ")) 
    bmi=(weight/(height*height))   
    print("Your BMI is ",(bmi))
    #print(f"BMI category: {category1}")
    if bmi<18.5:
        #print(f"BMI Category: {category1}")
        return f"BMI Category: {category1}"
    elif bmi>=18.5 and bmi<=24.9:
        #print(f"BMI Category: {category2}")
        return f"BMI Category: {category2}"
    elif bmi>=25.0 and bmi<=29.9:
        #print(f"BMI Category: {category3}")
        return f"BMI Category: {category3}"
    elif bmi>=30.0:
        #print(f"BMI Category: {category4}")
        return f"BMI Category: {category4}"
    else:
        #print("YOU ARE IN DANGER!")
        return "YOU ARE IN DANGER!"
height=float(input("Your height in m: "))
weight=float(input("Your weight in KG: "))        
check=bmi_calc(weight,height)
print(check)


#check2=check1(check)
#print(check2)
       """

