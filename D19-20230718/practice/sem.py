semester_details=[{"study":"B.tech",
                   "institute":"cape",
                   "semester_marks":[{"semester_name":1,
                                      "subjects":["computer programming","software engineer","operating system"],
                                      "semester_grade":"A",
                                      },
                                      {"semester_name":2,
                                       "subjects":["operating system","visual basic","oops"],
                                       "semester_grade":"B",
                                       },
                                      ]},
                    {"study":"M.tech",
                   "institute":"cape",
                   "semester_marks":[{"semester_name":1,
                                      "subjects":["computer programming","software engineer","operating system"],
                                      "semester_grade":"A",
                                      },
                                      {"semester_name":2,
                                       "subjects":["operating system","visual basic","oops"],
                                       "semester_grade":"B",
                                       },
                                       ]}]
for study in semester_details:
    education=study["study"]
    marks=study["semester_marks"]
    for i in marks:
        name=i["semester_name"]
        subject1=i["subjects"][0]
        subject2=i["subjects"][0]
        if name==1:
            print(subject1)
        elif name==2:
            print(subject2)
       