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
                               "percentage":43.7,
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


#my_name=my_resume["name"]
#my_education=my_resume["education"]
#print(my_education)
# for i in my_education:
#     percent=i["percentage"]
#     qualify=i["qualification"]
#     passed=i["passed_out_year"]
#     #print(percent)
#     if percent<50:
#         if passed>=2020:

#             print(f"{percent} You are eligible")
#     else:
#         print(f"{percent} You are not eligible")


personal=my_resume["personal_details"]
for j in personal["languages"]:
    print(j)