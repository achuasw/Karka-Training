#subject names
subject1="tamil"
subject2="english"
subject3="maths"
subject4="science"
#column name for subjects
a="subject"
#teacher names
teacher1="aswin"
teacher2="niwsa"
teacher3="achu"
teacher4="kumar"
#column name for teachers
b="teachers"
#print table line for up
print("+","-"*44,"+")
#print space in right side of subject and left side of teachers
print("|s|{:<25} |{:>16}".format(a,b),"|")
print("+","-"*44,"+")
print("|1|{:<25} |{:>16}".format(subject1,teacher1),"|")
print("|2|{:<25} |{:>16}".format(subject2,teacher2),"|")
print("|3|{:<25} |{:>16}".format(subject3,teacher3),"|")
print("|4|{:<25} |{:>16}".format(subject4,teacher4),"|")
#print table line for down
print("+","-"*44,"+")



