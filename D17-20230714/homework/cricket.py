
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

num=0
highest_score=0
for i in cricketers:
    #print(i)
    names=i["name"]
    century=i["centuries"]
    hat_trick=i["hat_trick"]
    highest=i["HS"]
    highest_score=highest+highest_score
    #print(highest)
    if century>10:
        num=num+1   
        #print("Number of players scored more than 10 centuries:",num)
    elif hat_trick>5:
        print(names)
    elif highest
    
        