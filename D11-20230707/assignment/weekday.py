def week_day(day):
    day=int(input("Enter the date:"))

    if day==0 or day==7:
        print("Today is Saturday")
    elif day==1:
        print("Today is Sunday")
    elif day==2:
        print("Today is Monday")
    elif day==3:
        print("Today is Tuesday")
    elif day==4:
        print("Today is Wednesday")
    elif day==5:
        print("Today is Thursday")
    elif day==6:
        print("Today is Friday")
    else:
        print("Error")

week_day(6)
    
