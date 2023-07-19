print("I will add up the numbers you give me.")
total=0
while True:
    number=int(input("Number: "))
    total=number+total
    if number!=0:
        print("The total number so far is:",total)     
    else: 
        print("\nThe total is:",total)
        exit()

   
       
    
     