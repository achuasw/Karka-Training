my_resume={ 
            "name":"aswin kumar",
            "e-mail":"achu0461@gmail.com",
            "mbl_no":9600363288,
            "soft_skills":["creativity","team work"],
            "hard_skills":["programming skills","web development"],
            "education":[{"qualification":"SSLC",
                              "percentage":91.1,
                              "passed_out_year":2018
                              },

                              {"qualification":"HSC",
                               "percentage":63.7,
                               "passed_out_year":2020
                               },
                               {"qualification":"B.sc computer sceince",
                                "percentage":78.6,
                                "passed_out_year":2023,}],
            "projects":[{
                        "project_type":"learning app",
                        "resources":["text book","audio","video"],
                        },
                        {"project_type":"e-commerce site",
                         "resources":["search box","voice"]
                         }],
                       
                                   
            "experience":[{
                        "company_name":"flow",
                        "role":"web developer",
                        "years_of_experience":2,
                        "place":"nagercoil",
                        },
                        {"company_name":"amazon",
                         "role":"software testing",
                         "years_of_experience":1,
                         "place":"chennai"
                         },
                         {"company_name":"zohoo",
                          "role":"developer",
                          "years_of_experience":1.5,
                          "place":"tenkasi"}],


            "hobbies":["playing cricket","cooking","coding"],
            "personal_details":{
                                "father_ name":"Ayyappan",
                                "father's_occupation":"business",
                                "languages":["tamil","english"],
                                "DOB":"22-10-2002",
                                "gender":"male",
                                "marital_status":"single",
                                "address":{"door_no":39,
                                "street":"vagaydi north car street,kottar",
                                "city":"nagercoil",
                                "district":"kanyakumari",
                                "state":"TamilNadu",
                                "pin_code":629002}
                                }}
#print(my_resume["education"])
for resume in my_resume["experience"]:
    #educate1=my_resume["education"]
    educate1=resume["place"]
    educate2=resume["company_name"]
    educate3=resume["role"]
    print(resume["place"])
    print(educate1)
    print(educate2)
    print(educate3)
    #detail=my_resume["personal_details"]["gender"]
    #print(detail)
detail=my_resume["personal_details"]["gender"]
print(detail)
print(my_resume["personal_details"]["address"]["door_no"])

   # detail2=resume["languages"]

   # print(detail2)


    

    


 