#fruits={"apple","orange","mango"}
#print(fruits)
#print(fruits)
#print(fruits)

"""file=open("/home/aswin/Documents/karka.txt","w")
data=file.write("i am aswin\ni am developer ")
print(data)
file.close()

file=open("/home/aswin/Documents/karka.txt","a")
data2=file.write("i am aswin\ni am developer")
print(data2)
file.close()"""

file=open("/home/aswin/Documents/karka.txt","r")
#data1=file.read()
#print(data1.split())
#data=file.read()
#print(data)
#print(file.read())
for line in file:
   print(line.split())
    