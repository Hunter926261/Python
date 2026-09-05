# Automorphic Number

# An Automorphic Number is a number whose square ends with the number itself.

def is_automorphic(n):
    n_sq = n*n

    digit_count_n = 0

    while n_sq:
        digit_count_n += 1
        n_sq //= 10

    return n == (n*n % (10*digit_count_n))

def main():
    while True:
        try:
            n = int(input("Enter n: "))

            if n <= 0:
                raise ValueError("Value must be positive integer")

            break
        except ValueError as error:
            print(f"Invalid Input, {error}")

    is_auto = is_automorphic(n)

    if is_auto:
        print(f"{n} is automorphic")
    else:
        print(f"{n} is not automorphic")


if __name__ == "__main__":
    main()