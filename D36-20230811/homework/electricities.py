
from pprint import pprint
consumer_data={"consumer_name":"aswin",
                   "eb_reading":[1100,1200,1350,1650,2050]
}

l=[]
read=consumer_data["eb_reading"]

for i in range(1,len(read)):
    total_rate=0
    unit=read[i]-read[i-1]
    month=i
    if unit<100:
        print("There is no rate to pay")
    elif unit>100 and unit<200:
        rate=unit*2
        total_rate=total_rate+rate
    elif unit>200 and unit<500:
        rate=unit*5
        total_rate=total_rate+rate
    elif unit>500 and unit<1000:
        rate=unit*10
        total_rate=total_rate+rate
    elif unit>=1000:
        rate=unit*14
        total_rate=total_rate+rate
    

    final_rate={"month":month,
                "total_amount":total_rate,
                  "unit_consumed":unit
                  }

    l.append(final_rate)
pprint(l)
    
        
    