# Title: Compute Pay with Overtime
# This program prompts the user for hours worked and rate per hour to compute gross pay with overtime

hour = int(input('Enter Hours Worked: '))
rph = int(input('Enter Rate per Hour: '))
gp = 0

def computePay(hoursWorked,Pay):
    gp = hoursWorked * Pay
    if hoursWorked > 40:
        withOvertime = (hoursWorked - 40) * (Pay/2)
        gp += withOvertime
    return(gp)


print('Pay:',computePay(hour,rph))