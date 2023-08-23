# Title: string and how many?
# This program returns a string that is n (non-negative integer) copies of a given string.

inp = input('input a string: ')
inp2 = input('How many copies do you like? ')

def larger_string(text, n):
   result = ""
   for i in range(n):
      result = result + text
   return result

print(larger_string(inp,inp2))