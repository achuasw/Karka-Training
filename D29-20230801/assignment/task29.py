dictionary=[{
             "name":"achu",
             "email":"achu0461@gmail.com",
             "password":"achu@223",
             "hobbies":["cooking","playing","watching TV"],
             "friends":["kumar","aswin"]
             },
             {
              "name":"kumar",
             "email":"kumar22@gmail.com",
             "password":"221067",
             "hobbies":["cooking","playing","watching TV"],
             "friends":["aswin","achu"]
             },
             {
             "name":"aswin",
             "email":"aswin6@gmail.com",
             "password":"672210",
             "hobbies":["cooking","playing","watching TV"],
             "friends":["achu","kumar"]
             }]
mail=input("Enter your email: ")
pwrd=input("Enter your password: ")
def logging_in(mail,pwrd):
    def hob(hobbys,friend):
        print(hobbys)
        for detail in friend:
            print(detail,",",end=" ")
        print()
           
    for i in dictionary:
        if mail==i["email"] and pwrd==i["password"]:
            i["logged in"]="true"   
        else:
            i["logged in"]="false"    
        print(i)
        print()
        
    hob("hobby",i["hobbies"])
    hob("friends_list",i["friends"])
logging_in(mail,pwrd)


