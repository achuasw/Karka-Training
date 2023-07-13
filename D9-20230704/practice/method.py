#.capitalize() [to convert the first character to upper case]
name="my name is aswin kumar"
print(name.capitalize())

#.casefold() [to convert string into lower case]
name="mY namE Is Aswin kUmar"
print(name.casefold())

#.center() [returns a centered string]
name="aswin"
print(name.center(20,"j"))

#.count() [return the number of times a specified value occurs in a string]
name="my name is aswin and my full name is aswin kumar"
print(len(name))
print(name.count("name"))

"""
#.endswith() [returns true if the string ends with the specified value and 
             false if the string not ends with the specified value]"""
name="my name is aswin and my full name is aswin kumar"
print(name.endswith("kumar",0,4))

"""
#.startwith() [returns true if the string starts with the specified value and 
             false if the string not starts with the specified value]"""
name="my name is aswin and my full name is aswin kumar"
print(name.startswith("my"))


#.replace()
name="aswin"
print(name.replace("aswin","achu"))

#.strip()
name="  my name is aswin"
print(name.strip())
