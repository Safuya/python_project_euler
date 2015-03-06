from math import *

testing_number = int(1)
sum_of_logs = log(2)

n = int(input('Choose a number: '))

while testing_number < n:
    testing_number = testing_number + 2
    
    for checking_number in range(2, testing_number):
        if testing_number % checking_number == 0:
            break
        
    else:
        sum_of_logs = sum_of_logs + testing_number
        print(sum_of_logs/n)

print('The sum of the logs is:', sum_of_logs)
