# Prime Numbers in a Range

# return all prime numbers between two given numbers.

def list_prime_numbers(n1:int,n2:int) -> list:
    # taking n1 < n2

    prime = []    

    for i in range(n1,n2+1):
        is_prime = True
        for j in range(2,i):

            if j <= 1:
                is_prime = False
                break

            if i%j == 0:
                is_prime = False
                break

        if is_prime:
            prime.append(i)


    return prime


def main():
    # user input

    while True:
        try:
            n1 = int(input("Enter 1'st value: "))
            n2 = int(input("Enter 2'nd value: "))

            if n1 <= 1 or n2 <= 1:
                raise ValueError("value must be positive")

            break

        except ValueError as error:
            print(f"Invalid Input, {error}")

    
    if n1 < n2:
        prime_numbers = list_prime_numbers(n1,n2)
    else:
        prime_numbers = list_prime_numbers(n2,n1)

    

    print(f"Prime numbers between {n1} & {n2} are {prime_numbers}")


if __name__ == "__main__":
    main()