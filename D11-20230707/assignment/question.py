"""age=int(input("Enter the age:"))
height=input("Enter the height:")
weight=float(input("Enter the weight:"))
print((f"so,you are {age} old, {height} tall and {int(weight)} heavy."))"""
import bmi

category1="underweight"
category2="normalweight"
category3="overweight"
category4="obese"

question=input("U:\My Documents\CompSci\> ")
old=int(input("How old are you? "))
tall=float(input("How tall are you? "))
weight=float(input("How much do you weigh? "))
print(f"So, you're {old}, {tall}m tall and {weight} KG.")
BMI=bmi.bmi_calculator(weight,tall)
print("and your BMI is",BMI)

if BMI<18.5:
    print(f"BMI Category: {category1}\n It is very kevalammm.....")
elif BMI>=18.5 and BMI<=24.9:
    print(f"BMI Category: {category2}\n It is correct weight")
elif BMI>=25.0 and BMI<=29.9:
    print(f"BMI Category: {category3}\n It is abnormal!")
elif BMI>=30.0:
    print(f"BMI Category: {category4}\n It is sothu moottaa..!")
else:
    exit()

print("U:\My Documents\CompSci\>")