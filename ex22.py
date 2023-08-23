# Title: is it near a thousand?
# This program tests whether a number is within 100 of 1000 or 2000.

inp = input('Input an Integer: ')

def nearThousand(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

print(nearThousand(inp))

