print("TWO QUESTIONS!\nThink of an object, and I'll try to guess it.")
print("\n")
question1=input("Question 1) Is it animal, vegetable, or mineral?\n")
if question1=="animal":
    question2=input("Question 2) Is it bigger than a breadbox?\n")
    print("\n")
    if question2=="no":
        print("My guess is that you are thinking of a moose.\nI would ask you if I'm right. but I don't actually care.")
        print("\n")
    else:
        print("wrong")
        print("\n")
elif question1=="mineral":
        question2=input("Question 2) Is it bigger than a breadbox?\n") 
        print("\n")
        if question2=="yes":
            print("My guess is that you are thinking of a truck.\nI would ask you if I'm right. but I don't actually care.")
            print("\n")
        else:
            print("wrong")
            print("\n")
elif question1=="vegetable":
     print("\n")
     print("wrong answer")
     