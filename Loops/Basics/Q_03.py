# Factorial 

def factorial(n):
    fact = 1

    for i in range(1,n+1):
        fact *= i

    return fact

def main():
    while True:
        try:
            n = int(input("Enter n (for factorial): "))

            if n < 0:
                raise ValueError("Value must be non-negative..")

            break

        except ValueError as error:
            print(f"Invalid Input, {error}")

    # call factorial function
    fact = factorial(n)

    print(f"Factorial of {n} is {fact}")

if __name__ == "__main__":
    main()