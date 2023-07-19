persnl_dtls=[{"name":"Aswin Kumar",
               "age":20,
               "place":"nagercoil",
            },
            {"name":"Devi Priya",
             "age":21,
            "place":"aralvaimozhi",
            
            },
            {"name":"reshma",
             "age":21,
            "place":"marthandam",
            },
            {"name":"rabin",
             "age":22,
            "place":"ramanputhur",
            
            },
            {"name":"kavish",
             "age":21,
            "place":"vadasery",
            
            },
            {"name":"rashika",
             "age":21,
             "place":"parasery",
             
             },
             {"name":"sulaebha",
              "age":22,
              "place":"panakudy",
              }]
def personal_details():
    for i,each_detail in enumerate(persnl_dtls):
        print("\n",str(i+1),") I am",each_detail["name"],",I am",each_detail["age"],"years old and I am from",each_detail["place"])
    """for each_detail in persnl_dtls:
        age=each_detail["age"]
        name=each_detail["name"]
        place=each_detail["place"]   """   
personal_details()  
def age_above():
    print("-"*60)
    print("\nAge above 21!")
    
    for i,each_detail in enumerate(persnl_dtls):
        if each_detail["age"]>21:
        #print(f"age above 21!\nname: {name}, \nplace: {place}")
            
            print("\n",str(i+1),") name:",each_detail["name"],"\n","    place:",each_detail["place"])
    

age_above()
        


#print("\nName and place of individuals whose age is above 21:")

#print(str(i+1),") I am",each_d,etail["name"],",I am",each_detail["age"],"years old and I am from",each_detail["place"])

    

"""for i,each_detail in enumerate(persnl_dtls):
    age=each_detail["age"]
    name=each_detail["name"]
    place=each_detail["place"]
    print(f"\nI am {name}, I am {age} years old and I am from {place}. ")  
    if age>21:
        print(f"name: {name}, place: {place}")
    else:
        continue
    """
      
