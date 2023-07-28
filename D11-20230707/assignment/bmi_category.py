import bmi
category1="under weight"
category2="normal weight"
category3="over weight"
category4="obese"

heigh=float(input("Your height in m: "))
weigh=float(input("your weight in KG: "))
a=bmi.bmi_calculator(weigh,heigh)
print("Your BMI is:",a)
if a<18.5:
    print(f"BMI Category: {category1}")
elif a>=18.5 and a<=24.9:
    print(f"BMI Category: {category2}")
elif a>=25.0 and a<=29.9:
    print(f"BMI Category: {category3}")
elif a>=30.0:
    print(f"BMI Category: {category4}")
else:
    print("YOU ARE IN DANGER!")
