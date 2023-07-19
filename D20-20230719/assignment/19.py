items_list = [
    {'name': 'Apple', 'category': 'Fruits'},
    {'name': 'Carrot', 'category': 'Vegetables'},
    {'name': 'Banana', 'category': 'Fruits'},
    {'name': 'Broccoli', 'category': 'Vegetables'},
]
fruits=[]
vegtables=[]
store={"fruit":[],"vegtable":[]}    
print(store["fruit"])
#fruit1=items_list[0]["name"]
#fruit2=items_list[2]["name"]
#fruit3=fruit1,fruit2


#veg1=items_list[1]["name"]
#veg2=items_list[3]["name"]
#veg3=veg1,veg2
#vegtables.append(veg3)
#print(vegtables)
#print(fruit1)
#print(fruit2)
#fruits.append(fruit3)
#print("fruits;",fruits)
#add=fruits+vegtables
#print(add)
for names in items_list:
    if names["category"]=="Fruits":
       fruits.append(names["name"])
       
    if names["category"]=="Vegetables":
        vegtables.append(names["name"])

print(store)  
    

    
