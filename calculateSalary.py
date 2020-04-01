#CIS40 - Chapter 4 Exercise 2 - Priya Pradeep
#Program that prompts the user for hours and rate to compute
#gross pay using try and except so that the program handles non-numeric
#input gracefully.
#
import random

OVERTIME_RATE = 1.5
HOUR_WORKED = 40

company = input('Enter your company name:').strip()
while True:
    
    try:
        hours = float(input('Enter the hours you have worked in a week:'))
        if hours >= 0:
            try:
                rate = float(input('Enter the rate:'))
                if rate >= 0:
                    try:
                        if hours > HOUR_WORKED:
                            extraHours = hours - HOUR_WORKED
                            pay = HOUR_WORKED * rate + extraHours * 10 * OVERTIME_RATE
                            print('Company name:', company.strip())
                            print('Hours:', hours)
                            print('Rate:', rate)
                            print('************************************')
                            print('Your document number is:', random.randint(1000,2000))
                            print('Your ', company, ' gross pay is $', round(pay,2), '.')
                        else:
                            pay = hours * rate
                            print('Company name:', company.strip())
                            print('Hours:', hours)
                            print('Rate:', rate)
                            print('************************************')
                            print('Your document number is:', random.randint(1000,2000))
                            print('Your', company, ' gross pay is $', round(pay,2), '.')

                    except:
                        print('Error, please enter a numeric value.')
            except:
                print('Error, please enter a numeric value.')
    except:
        print('Error, please enter a numeric value.')

"""
OUTPUT 1:
Enter your company name:google
Enter the hours you have worked in a week:45
Enter the rate:10
Company name: google
Hours: 45.0
Rate: 10.0
************************************
Your document number is: 1030
Your  google  gross pay is $ 475.0 .

OUTPUT 2:
Enter your company name:apple
Enter the hours you have worked in a week:55
Enter the rate:10
Company name: apple
Hours: 55.0
Rate: 10.0
************************************
Your document number is: 1325
Your  apple  gross pay is $ 625.0 .

OUTPU 3:
Enter your company name:microsoft
Enter the hours you have worked in a week:-50
Enter the hours you have worked in a week:-34
"""
