prime_count = int(1)  # counting 2 already so we can be more efficient..

for testing_number in range(3, 100000001, 2):
    for checking_number in range(2, testing_number):
        if testing_number % checking_number == 0:
            break
    else:
        prime_count += 1
        if prime_count > 999:
            print('1000th prime: ',testing_number)
            break
