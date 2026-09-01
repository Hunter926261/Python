# Prime Number

# A prime number is a positive integer greater than 1 that has exactly two factors: 1 & itself

def is_prime(n):
    prime = True

    if n == 1:
        return False

    for i in range(2,n):
        if n % i == 0:
            prime = False 
            break

    return prime


def main():
    while True:
        try:
            # user input
            n = int(input("Enter n(to check is prime): "))

            if n <= 0:
                raise ValueError("n must be the positive integer")

            break

        except ValueError as error:
            print(f"Invalid Input, {error}")

    prime_check = is_prime(n)

    if prime_check:
        print(f"{n} is prime number")
    else:
        print(f"{n} is not prime number")

if __name__ == "__main__":
    main()