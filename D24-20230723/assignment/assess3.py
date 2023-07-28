monthly_gold_rate=[{"month_name":"january",
                    "gold_rate":1500,
                    "jwell_list":[{"name":"chain",
                                   "making_cost":12},
                                   {"name":"ring",
                                    "making_cost":14}]
                    },
                    {"month_name":"february",
                    "gold_rate":2000,
                    "jwell_list":[{"name":"chain",
                                   "making_cost":14},
                                   {"name":"ring",
                                    "making_cost":10}]
                    },
                    {"month_name":"march",
                    "gold_rate":1000,
                    "jwell_list":[{"name":"chain",
                                   "making_cost":10},
                                   {"name":"ring",
                                    "making_cost":12}]
                    },
                    {"month_name":"april",
                     "gold_rate":1100,
                     "jwell_list":[{"name":"chain",
                                    "making_cost":20},
                                    {"name":"ring",
                                     "making_cost":12}]}
                    ]
#max_month=monthly_gold_rate[0]["month_name"
for month in monthly_gold_rate:
    #app=[]
    temp={}
    months=month["month_name"]
    rate=month["gold_rate"]
    jwells=month["jwell_list"]
    temp['month']=months
    temp['gold_rate']=rate
    #print(rate)
    for jwell in jwells:
        names=jwell["name"]
        cost=jwell["making_cost"]
        add=rate*cost/100
        total_rate=rate+add
        temp[names]=total_rate
    print(temp)
    
    

            
    #print(temp)

        # dict={"month":months,"gold_rate":rate,"chain_rate":total_rate,"ring_rate":total_rate}
        # print(dict)
        

    