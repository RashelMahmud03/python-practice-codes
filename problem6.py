#Write a Python function to check if a given string is a palindrome or not.
st_r=input("Enter the string:::::::")
new_str=st_r[::-1]
if (st_r==new_str):
    print("palindrome")
else:
    print("not palindrome")