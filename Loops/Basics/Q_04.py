# Reverse a Number

def reverse_number(n):

    # reverse number 
    rev = 0
    while n:
        rev *= 10
        rev += n%10  # last number

        # update original number
        n //= 10

    return rev

def main():
    while True:
        # User Input
        try:
            n = int(input("Enter n(For reversing a number): "))

            if n < 0:
                raise ValueError("n must be positive")

            break

        except ValueError as error:
            print(f"Invalid Input, {error}")

    print(f"Reverse of {n} is {reverse_number(n)}")

if __name__ == "__main__":
    main()