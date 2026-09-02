# Fibonacci Series

# A Fibonacci series is a sequence where every number is the sum of the previous two numbers.
# strat with 0 & 1
# ex. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# function which return the first n Fibonacci Series

def fibonacci_series(n):
    n1, n2 = 0, 1

    series = []

    if n == 0:
        return series

    if n >= 1:
        series.append(n1)
        

    if n >= 2:
        series.append(n2)


    if (n-2) > 0:
        for i in range(0,n-2):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            series.append(n3)


    return series
    
    
def main():
    while True:
        try:
            n = int(input("Enter n(for 1st n fibonacci series): "))

            if n < 0:
                raise ValueError("n must be non-negative interger")

            break

        except ValueError as error:
            print(f"Invalid Input, {error}")

    series = fibonacci_series(n)

    print(f"first {n} Fibonacci Series: {series}")

if __name__ == "__main__":
    main()