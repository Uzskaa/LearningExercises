# Title: Odd or Even?
# This program determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.

inp = input('Enter a Number: ')

try:
    rem = int(inp)%2
    if rem == 0:
        print("the number is EVEN")
    else:
        print("the number is ODD")
except:
    print("You have not enetered a number")