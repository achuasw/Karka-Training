# eval()
a="aswin"
b="kumar"
print(eval("a+b"))

#eval using global variables
x=100
y=200
print(eval("x+y",{"x":x,"y":y}))

#format()
print(format(22,"%"))

#id()
#x=[1,2,3,4,4]
print(id(2))

#len
a="string"
print(len(a))

#max()
print(max("aswi","asws"))
print(max("pavi","thra"))

name="my name is aswin kumar"
print(name.capitalize())

#.casefold() [to convert string into lower case]
name="mY namE Is Aswin kUmar"
print(name.casefold())

#.center() [returns a centered string]
name="aswin"
print(name.center(20,"j"))
#.capitalize() [to convert the first character to upper case]

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

#slice()
a=(22,10,2,6,7,5,0,9)
b=slice(1)
print(a[b])