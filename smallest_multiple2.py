


def main():
    max_value = 20
    for x in range(1, max_value+1):
        print(prime_fac(x))


def prime_fac(num):
    prime_factors = []
    i = 2

    while(i * i < num):
        while(num % i == 0):
            prime_factors.append(i)
            num = num / i
        i += 1
    if num > 1:
        prime_factors.append(num)

    return(prime_factors)


if __name__ == "__main__": main()
