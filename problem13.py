'''
#Write a Python program that takes a student’s percentage as input and prints their corresponding
 grade according to the following criteria: – 90% or above: A+ – 80-89%: A – 70-79%: B – 60-69%: C – Below 60%: Fail'''
per_mark=float(input("enter your percantage::"))
if(per_mark>=90 and per_mark<=100):
    print("A+")
elif(per_mark>=80 and per_mark<=89):
    print("A")
elif(per_mark>=70 and per_mark<=79):
    print("B")
elif(per_mark>=60 and per_mark<=69):
    print("C")
elif(per_mark<60):
    print("FAIL")
else:
    print("invalid input")