#Title:
#This program prompts the user for hours worked and rate per hour to compute gross pay

hour = int(input('Enter Hours Worked: '))
rph = int(input('Enter Rate per Hour: '))

gp = hour * rph

print('Pay:',gp)