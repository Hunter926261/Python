# LCM of two numbers

# Formula: 
#           LCM = (a × b) / GCD(a, b)

from Q_04 import gcd

def lcm(a,b):
    # LCM = (a x b) / GCD(a,b)

    return (a * b) / gcd(a,b)

def main():
    # user input
    while True:
        try:
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))

            if a <= 0 or b <= 0:
                raise ValueError("Value must be positive interger")

            break
        except ValueError as error:
            print(f"Invalid Input, {error}")

    print(f"LCM of {a} & {b} is {lcm(a,b)}")


if __name__ == "__main__":
    main()