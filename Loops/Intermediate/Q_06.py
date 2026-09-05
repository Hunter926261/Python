# Perfect Number

# A perfect number is a positive integer that is equal to the sum of its proper divisors (divisors excluding the number itself).

import math

def is_perfect_number(n:int) -> bool:
    s = 1 

    for i in range(2,math.isqrt(n) + 1):
        if n % i == 0:
            s += i

            pair = n // i
            if pair != i:
                s += pair

    return s == n

def main():
    while True:
        try:
            n = int(input("Enter n: "))

            if n <= 0:
                raise ValueError("n must be positive integer")

            break
        except ValueError as error:
            print(f"Invalid input, {error}")

    is_perfect = is_perfect_number(n)

    if is_perfect:
        print(f"{n} is perfect number")
    else:
        print(f"{n} is not perfect number")

if __name__ == "__main__":
    main()