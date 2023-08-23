# Title: return times 3
# This program calculates the sum of three given numbers. If the values are equal, return three times their sum.

inp = input('input number first number: ')
inp2 = input('input number second number: ')
inp3 = input('input number three number: ')
all = 0

def ifTimesThree(x,y,z):
    
    all = x + y + z

    if (x == y == z ):
        all*3

print(all)