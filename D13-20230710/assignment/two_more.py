print("TWO MORE QUESTIONS, BABY!")
print("\n")
print("Think of something and I'll try to guess it!")
inside_alive="houseplant"
inside_not_alive="shower curtain"
outside_alive="bison"
outside_not_alive="billboard"
both_alive="dog"
both_not_alive="cell phone" 
qn1=input("Question 1) Does it stay inside or outside or both? ")
qn2=input("Question 2) Is it a living thing? ")
def two_qn(qn1,qn2):
    if qn1=="outside" and qn2=="yes":
            print("\n")
            print(outside_alive)
    if qn1=="outside" and qn2=="no":
        print("\n")
        print(outside_not_alive)
    if qn1=="inside" and qn2=="yes": 
            print("\n")
            print(inside_alive)
    if qn1=="inside" and qn2=="no":
          print("\n")
          print(inside_not_alive)
    if qn1=="both" and qn2=="yes":
          print("\n")
          print(both_alive)
    if qn1=="both" and qn2=="no":
          print("\n")
          print(both_not_alive) 
two_qn(qn1,qn2)