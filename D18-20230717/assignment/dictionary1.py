grp_join=[{"name":"aswin kumar",
           "place":"nagercoil",
           "marks":{"tamil":96,
                    "english":89,
                    "maths":86,
                    "science":95,
                    "social":92}
            },
            {"name":"devipriya",
             "place":"aralvaimozhi",
             "marks":{"tamil":90,
                      "english":85,
                      "maths":99,
                      "science":78,
                      "social":84}},
            {"name":"reshma",
             "place":"marthandam",
             "marks":{"tamil":88,
                      "english":95,
                      "maths":100,
                      "science":88,
                      "social":94}},
            {"name":"rabin",
             "place":"ramanputhur",
             "marks":{"tamil":50,
                      "english":67,
                      "maths":100,
                      "science":98,
                      "social":80}},
            {"name":"kavish",
             "place":"vadasery",
             "marks":{"tamil":95,
                      "english":88,
                      "maths":100,
                      "science":88,
                      "social":94}},
            {"name":"arun",
             "place":"parasery",
             "marks":{"tamil":11,
                      "english":85,
                      "maths":100,
                      "science":10,
                      "social":10}},]


for groups in grp_join:
    name=groups["name"]
    tamil=groups["marks"]["tamil"]
    english=groups["marks"]["english"]
    maths=groups["marks"]["maths"]
    science=groups["marks"]["science"]
    social=groups["marks"]["social"]
    total=tamil+english+maths+science+social

    print(f"\nTotal of {name}")
    print(total)

    percentage=(total/500)*100

    print(f"\nPercentage of {name}")
    print(percentage)

    if percentage>90 or (maths>=98 and percentage>80 and percentage<=90):
        print(f"\n{name} is Eligible for maths group")

    elif percentage>80 or (maths>=98 and percentage>70 and percentage<80):
        print(f"\n{name} is eligible for computer science")
    
    else:
        print("You are not eligible for these courses!")
    

    
                          
                      