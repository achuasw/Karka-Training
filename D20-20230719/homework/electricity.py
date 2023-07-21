def calculate_electricity_bill():
    consumer_data={"consumer_name":"aswin",
                   "eb_reading":[1100,1200,1350,1650,2050]
    } 
    total_unit=[]
    total_amount=0
    reading=consumer_data["eb_reading"]
    #print(reading)

    for i in range(1,len(reading)):
        #print(i)
        unit=reading[i]-reading[i-1]
        #print(unit)
        month=i
        if unit<100:
            print("no amount to pay")
        # elif unit==100:
        #     rate=2*unit
        #     total_amount=total_amount+rate
            #data={"month":month,"units_consumed":unit,"bill_amount":rate}
            #print(data)
        elif unit>=100 and unit<200:
            rate=2*unit
            total_amount=total_amount+rate
           # data={"month":month,"units_consumed":unit,"bill_amount":rate}
           # print(data)
        elif unit>=200 and unit<500:
            rate=5*unit
            total_amount=total_amount+rate
        elif unit>=500 and unit<1000:
            rate=10*unit
            total_amount=total_amount+rate
        elif unit>=1000:
            rate=14*unit
            total_amount=total_amount+rate
            #data={"month":month,"units_consumed":unit,"bill_amount":rate}
           # print(data)
        data={"month":month,
              "units_consumed":unit,
              "bill_amount":rate}
    
        total_unit.append(data)
  


#options=input("Enter the option: ")


    
  
    print(total_unit)
#file1=open("/home/aswin/Documents/aswinkumar.txt","w")
#for line in a:
        #print(units)
 #   data=file1.write(f"month:{line['month']},\nunits_consumed:{line['units_consumed']},\nbill_amount:{line['bill_amount']}\n") 
    #print(data)
    #print("\nTotal amount= ",total_amount)
#print(data)
#file1.close()
    file1=open("/home/aswin/Documents/aswinkumar.txt","r")
    data=file1.read()

    print(data)



    
    
         
    
   

        

        
       
       
calculate_electricity_bill()

    