monthly_gold_rate=[{"month_name":"january",
                    "gold_rate":221500
                    },
                    {"month_name":"february",
                    "gold_rate":2000
                    },
                    {"month_name":"march",
                    "gold_rate":1000
                    },
                    {"month_name":"april",
                     "gold_rate":11111100}
                    ]
total_rate=[]
max_value=monthly_gold_rate[0]["gold_rate"]
#after if conditon max_value=maximum number
max_month=monthly_gold_rate[0]["month_name"]
min_value=monthly_gold_rate[0]["gold_rate"]
min_month=monthly_gold_rate[0]["month_name"]
for month in monthly_gold_rate:
    rate=month["gold_rate"]
    total_rate.append(rate)
print(total_rate)
"""months=month["month_name"]
    if rate>max_value:
        max_value=rate
        max_month=months
    elif rate<min_value:
        min_value=rate
        min_month=months

print("max=",max_value,max_month)
print("min=",min_value,min_month)"""
     

    

    


"""month1=monthly_gold_rate[0]["gold_rate"]
month2=monthly_gold_rate[1]["gold_rate"]
month3=monthly_gold_rate[2]["gold_rate"]
month4=monthly_gold_rate[3]["gold_rate"]

rate1=monthly_gold_rate[0]["month_name"]
rate2=monthly_gold_rate[1]["month_name"]
rate3=monthly_gold_rate[2]["month_name"]
rate4=monthly_gold_rate[3]["month_name"]"""



"""if month1<month2 and month1<month3 and month1<month4:
    print(month1,rate1)
elif month2<month1 and month2<month3 and month2<month4:
    print(month2,rate2)
elif month3<month1 and month3<month2 and month3<month4:
    print(month3,rate3)
elif month4<month1 and month4<month2 and month4<month3:
    print(month4,rate4)"""