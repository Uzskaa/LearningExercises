# Title: File Extension return
# This program accepts a filename from the user and prints the extension of the file.

payl = input('input filename:')
extension = payl.split('.')
print("Extension of the file is",repr(extension[-1]))
