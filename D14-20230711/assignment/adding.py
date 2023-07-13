print("I will add up the numbers you give me.")
total=0
while True:
    number=int(input("Number: "))
    total=number+total
    print("The total number so far is:",total)
    if total==0:
        print("\nTotal sum is:",total)
        exit()
    
     