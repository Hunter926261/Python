# Multiplication table

def multiplication_table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

def main():
    while True:
        try:
            n = int(input("Enter n (for table): "))

            if n <= 0:
                raise ValueError("Invalid Input, Value must be non-zero and non-negative integer")

            break

        except ValueError as error:
            print(f"Invalid Input, {error}")

    # multiplication function is called
    multiplication_table(n)


if __name__ == "__main__":
    main()