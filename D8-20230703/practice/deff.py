"""def calc_interest(principle,no_of_years,rate_of_interest):
    I=principle*no_of_years*rate_of_interest/100
    return I
prncpl=int(input("Enter the principle:"))
no_of_yrs=int(input("Enter the no.of years:"))
rate_of_intrst=int(input("Enter the rate of interest:"))
interest=calc_interest(prncpl,no_of_yrs,rate_of_intrst)
print(interest)
"""
def is_eligibility(passed_out_year):
    year=passed_out_year>2021
    return year
pass_out_year=int(input("Enter the year:"))
year1=is_eligibility(pass_out_year)
print(year1)
"""
def twice(a):
    num=a*2
    return num
a=int(input("Enter the number:"))
b=twice(a)
print(b)"""

def is_eligible(passed_out_year):
    if passed_out_year>2021:
        return True
    else:
        return False
passed_out_year=int(input("Enter the year"))
year=is_eligible(passed_out_year)  
print(year)


"""def process_list(my_list):
    for i,item in enumerate(my_list):
        if i>3:
            print(item)
            break
        else:
            continue
my_list=(input("Enter the list:"))
process_list(my_list)
"""

    




