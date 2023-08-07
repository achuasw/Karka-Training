# string="the quick brown fox jumps over the lazy dog the quick brown fox"
# list=string.split()
# the=0
# quick=0
# brown=0
# fox=0
# jump=0
# over=0
# lazy=0
# dog=0
# for i in list:
#     if i=="the":
#         the=the+1
#     elif i=="quick":
#         quick=quick+1
#     elif i=="brown":
#         brown=brown+1
#     elif i=="fox":
#         fox=fox+1
#     elif i=="jumps":
#         jump=jump+1
#     elif i=="over":
#         over=over+1
#     elif i=="lazy":
#         lazy=lazy+1
#     elif i=="dog":
#         dog=dog+1
    
# dict={"the":the,"quick":quick,"brown":brown,"fox":fox,"jump":jump,"over":over,"lazy":lazy,"dog":dog}
# print(dict)


string="the quick brown fox jumps over the lazy dog the quick brown fox"
list=string.split()
dict={}
for i in list:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print(dict[i])
        

    

  
       
