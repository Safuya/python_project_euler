def main():
    max_number = 21
    test_number = max_number - 1

    while(divisible_by_all(test_number, max_number) != True):
        test_number += max_number - 1

    print(test_number, "is the first divisible by all")


def divisible_by_all(num, max_num):
    for x in range(1, max_num):
        if(num % x != 0):
            return False

    print("Testing for divisibility")
    return True


if __name__ == "__main__": main()
