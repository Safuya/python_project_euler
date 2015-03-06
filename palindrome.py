def main():
    result = 0

    for x in range(100, 1000):
        for y in range(100, 1000):
            if(palindrome_check(x*y) and result < x*y):
                result = x*y

    if result != 0:
        print(result)
    else:
        print("No palindrome found.")


def palindrome_check(num):
    num = str(num)
    return num == num[::-1]


if __name__ == "__main__": main()
