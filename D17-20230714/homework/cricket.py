
cricketers=[{"name":"Virat kohli",
             "country":"India",
             "centuries":75,
             "half_centuries":124,
             "wickets":4,
             "hat_trick":0,
             "HS":[254,205,100,73,45]},

             {"name":"Steven smith",
             "country":"Australia",
             "centuries":43,
             "half_centuries":70,
             "wickets":3,
             "hat_trick":0,
             "HS":[239,201,197,101,68]},
             
            {"name":"Ben stokes",
             "country":"England",
             "centuries":16,
             "half_centuries":51,
             "wickets":115,
             "hat_trick":2,
             "HS":[258,250,195,154,86]},
                  
            {"name":"Rashid khan",
             "country":"Afghanistan",
             "centuries":0,
             "half_centuries":3,
             "wickets":547,
             "hat_trick":7,
             "HS":[60,55,43,22,10]},  
             
             {"name":"Shaheen afridi",
             "country":"Pakistan",
             "centuries":0,
             "half_centuries":0,
             "wickets":233,
             "hat_trick":6,
             "HS":[23,19,20,6,10]}]

def centuries(cricketers):
    sum=0
    
    print("SCORED MORE THAN 10 CENTURIES:")
    for i,cricketer in enumerate(cricketers):
        #centuries=sum+centuries


   # print(cricketer["name"])
        name=cricketer["name"]
        #country=cricketer["country"]
        centuries=cricketer["centuries"]
        #half_centuries=cricketer["half_centuries"]
        #wickets=cricketer["wickets"]
        #hat_trick=cricketer["hat_trick"]
        #highest_score=cricketer["HS"]
    #print(f"\nI am {name},i am represented for {country} and i score {centuries} centuries and {half_centuries} half centuries in international cricket and i have {wickets} wickets in my career ,i have {hat_trick} hat tricks and my highest score is {highest_score}.")
        if centuries>10:
            
            print("\n",sum)
    print("-"*20)        
    print("\nMORE  THAN 5 HAT-TRICK WICKETS:")
    for cricketer in (cricketers):  
        name=cricketer["name"] 
        hat_trick=cricketer["hat_trick"]
        if hat_trick>5:
            print("\n",name)
    print("-"*30)
    print("\nTop batting score:\n\nName\t\tHighest Score\n")
    print("-"*29)
    highest_score=0
    for i,cricketer in enumerate(cricketers):
        sum=cricketer["HS"][0]
        print(sum)
    
        






            
    
    

        
       

    
centuries(cricketers)
        
    