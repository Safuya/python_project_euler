sum_of_multiples = 0

for tested_number in range(1,1000):
    if tested_number % 3 == 0:
        sum_of_multiples = sum_of_multiples + tested_number
    elif tested_number % 5 == 0:
        sum_of_multiples = sum_of_multiples + tested_number

print(sum_of_multiples)
