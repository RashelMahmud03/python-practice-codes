
#this is the code for understand recursion
def recursion(n):
    if (n==0):
        return
    print(n)
    recursion(n-10)
recursion(100)