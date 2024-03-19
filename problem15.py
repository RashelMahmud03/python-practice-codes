#Write a Python program that takes the time in hours (24-hour format) as input and prints “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night” based on the time.
time=float(input("enter your time:"))
if(time>=6 and time<=12):
    print("Good Morning")
elif(time>12 and time<=16):
    print("Good Afternoon")
elif(time>16 and time<=18):
    print("Good Evening")
elif(time>18 and time<=24):
    print("Good Night")
else:
 print("invalid input")