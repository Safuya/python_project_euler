def main():
    max = 101
    print(square_of_sum(max) - sum_of_squares(max))


def sum_of_squares(max):
    answer = 0
    for i in range(1, max):
        answer = i**2 + answer

    return(answer)


def square_of_sum(max):
    answer = 0
    for i in range(1, max):
        answer = i + answer

    return(answer**2)


if __name__ == "__main__": main()
