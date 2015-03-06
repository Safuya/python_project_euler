testing_number = int(1)
prime_count = int(1)
max_number = 10000

while prime_count <= max_number:
    testing_number = testing_number + 2
    
    for checking_number in range(2, testing_number):
        if testing_number % checking_number == 0:
            break
        
    else:
        prime_count += 1
        
        if prime_count > max_number:
            print("10001th prime: ",testing_number)

##step by step,
##
##1. Define array to hold prime numbers.
##2. populate prime numbers array with '2'.
##3. set first prime candidate to '3'
##4. set test limit to square root of prime candidate.
##5. Check if prime candidate is divisible by numbers in prime array. (upper limit for testing prime number<=root from step 4.) If divisible discard else add to prime numbers array.
##6. increment prime candidate by 2.
##7. goto step 4.
