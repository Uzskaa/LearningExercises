# Title: n+nn+nnn
# This program accepts an integer (n) and computes the value of n+nn+nnn.

inp = input("Input and integer: ")
in2 = str(inp + inp)
in3 = str(inp + inp + inp)

all = int(inp) + int(in2) + int(in3)

print(all)