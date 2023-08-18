# Title: Numbers until done!
# This program asks for a number until the user says done. If the user enters anything other than a number it detects it and prints an error message

answer = 0
total = 0
while(answer!="done"):
    answer = input('Enter a number: ')
    
    try:
        isit = int(answer)
        total = total + isit
    except:
        if(answer=='done'):
            print(total)
        else:
            print('Invalid Input')
    
    