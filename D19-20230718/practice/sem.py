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
    detail=study["semester_marks"]
    print(detail)
    print(study["study"])