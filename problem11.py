#Write a Python program that takes three numbers as input and prints the largest among them.
num1=int(input("Enter the value1:"))
num2=int(input("Enter the value2:"))
num3=int(input("Enter the value3:"))
if(num1>num2 and num1>num3):
    print("num1 is largest")
elif(num2>num1 and num2>num3):
    print("num2 is largest")
elif(num3>num1 and num3>num2):
    print("num3 is largest")
elif(num1==num2==num3):
    print("all are equal")
elif(num1==str or num2==str or num3==str):
