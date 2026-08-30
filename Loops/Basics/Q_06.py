# Check Palindrome Number

# A number is a palindrome if it reads the same forward and backward.

def is_palindrome(n):
    original_number = n
    rev_num = 0

    while n:
        rev_num *= 10
        rev_num += n%10

        n //= 10

    return original_number == rev_num

def main():
    while True:
        try:
            # user input
            n = int(input("Enter n(For checking the Palindrome): "))

            if n < 0:
                raise ValueError("n should not be negative")

            break

        except ValueError as error:
            print(f"Invalid Input, {error}")

    is_palin = is_palindrome(n)

    if is_palin:
        print(f"{n} is Palindrome")
    else:
        print(f"{n} is not Palindrome")


if __name__ == "__main__":
    main()