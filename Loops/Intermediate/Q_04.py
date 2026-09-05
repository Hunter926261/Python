# Find GCD of Two Numbers

def gcd(a,b):
    # Euclidean Algorithm
    while b != 0:
        remainder = a%b
        a = b
        b = remainder

    return a

def main():
    # user Input
    while True:
        try:
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))

            if a <= 0 or b <= 0:
                raise ValueError("value must be positive integer")

            break

        except ValueError as error:
            print(f"Invalid Input, {error}")

    print(f"GCD of {a} & {b} is {gcd(a,b)}")


if __name__ == "__main__":
    main()