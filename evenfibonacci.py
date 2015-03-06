sum_of_evens = 0
fibonacci = 1
last_number = 0
new_last_number = 0

while fibonacci <= 4000000:
    if fibonacci % 2 == 0:
        sum_of_evens += fibonacci

    temp_last_number = fibonacci
    fibonacci = last_number + fibonacci
    last_number = temp_last_number

print(sum_of_evens)
