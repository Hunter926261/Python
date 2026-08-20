# Sum of N numbers

def sum_of_n(n):
    add = 0
    for i in range(0,n+1):
        add += i

    return add

def main():
    while True:
        try:
            n = int(input("Enter n: "))

            if n < 0:
                raise ValueError("Invalid Input, n must be non-negative")

            break

        except ValueError as error:
            print(f"Invalid Input, {error}")

        

    addition = sum_of_n(n)

    print(f"Sum of n numbers is {addition}")

if __name__ == "__main__":
    main()