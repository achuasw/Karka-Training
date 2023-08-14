# num="0,1,2,3,4,5,6,7,8,9"
# low="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
# up=low.upper()
# spcl="!@#$%^&*()"
# all=num+low+up+spcl

# pwrd=(input("Enter the password: "))
# count=0
# string=""
# for i in pwrd:  
#     # if i in all:
        
#         if i.isupper():
#              string=string+i
#         elif i.islower():
#              string=string+i
#         elif i.isdigit():
#             string=string+i
#         else:
#             print("password must contain one lower case and one upper case and one digit")
               
# if len(string)<6 and i:
#     print("weak")
# elif len(string)>=6 and len(string)<=10:
#     print("moderate")
# elif len(string)>=11 and len(string)<=15:
#     print("strong")
# elif len(string)>15:
#     print("very strong")

pwrd=input("Enter the password: ")

def pwd(pwrd):
    is_uppercase = False
    is_lowercase = False
    is_digit = False

    for i in pwrd:
        if i.isupper():
            is_uppercase=True
        elif i.islower():
            is_lowercase=True
        elif i.isdigit():
            is_digit=True

    if not (is_uppercase and is_lowercase and is_digit):
        return "Password must contain atleast one upper case letter, one lower case letter and one digit"
    elif len(pwrd) < 6:
        return "Weak password, Try another password"
    elif len(pwrd) >=6 and len(pwrd) <=10:
        return "Moderate password"
    elif len(pwrd) >=11 and len(pwrd) <15:
        return "Strong password"
    elif len(pwrd) >=15:
        return "Very strong password"
    
print(pwd(pwrd))


 
