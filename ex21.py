# Title: what the difference?
# This program calculates the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.


inp = input('Input an Integer: ')

def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 
    
print(difference(inp))