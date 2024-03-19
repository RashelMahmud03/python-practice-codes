#Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.
num=int(input("Enter your number::"))
if (num<=-1):
    print("negative")
elif(num>0):
    print("positive")
elif (num==0):
    print("zero")