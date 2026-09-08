import math
import numpy as np

# Star Triangle
def star_triangle(n):
    for i in range(1,n+1):
        for j in range(0,i):
            print("*",end="")
        print()

# star_triangle(3)

# Reverse Star Triangle
def reverse_star_triangle(n):
    for i in range(n,0,-1):
        for j in range(0,i):
            print("*",end="")
        print()

# reverse_star_triangle(3)

# Pyramid Triangle
def star_pyramid(n):
    for i in range(1,n+1):
        print((n-i)*" ",end="")
        for j in range(0,i):
            print("*",end=" ")
        print()

# star_pyramid(5)

# Reverse Pyramid
def reverse_star_pyramid(n):
    for i in range(n,0,-1):
        print((n-i)*" ",end="")
        for j in range(0,i):
            print("*",end=" ")
        print()

# reverse_star_pyramid(5)

# Hollow Square
def hollow_square(n):
    for i in range(1,n+1):
        if i == 1 or i == n:
            print("* "*n)
        else:
            print("* " + "  "*(n-2) + "*")

# hollow_square(10)

import math
# Diamond
def diamond(n):
    # Uppar part of diamond
    for i in range(1,math.ceil(n/2) + 1):
        print(" " * (math.ceil(n/2) - i),end="")
        for j in range(0,i):
            print("*",end=" ")
        print()

    # Lower part of diamond
    for i in range(math.floor(n/2),0,-1):
        print(" " * (math.floor(n/2) - i),end="")
        for j in range(0,i):
            print(" *",end="")

        print()

# diamond(7)

# Pascal's triangle
def pascal_triangle(n):
    for i in range(0,n):
        print(" " * (n-i-1),end="")
        for j in range(0,i+1):
            print(math.comb(i,j),end=" ") # C(n, r) = n! / (r! × (n-r)!)

        print()

# pascal_triangle(5)

# Flody Triangle
def flody_triangle(n):
    s = 1
    for i in range(1,n+1):
        for j in range(0,i):
            print(s,end=" ")
            s += 1
        print()

# flody_triangle(5)

# Number palindrome Pyramid
def palindrome_pyramid(n):
    for i in range(1,n+1):
        print(" " * (n-i),end="")
        # Left
        for j in range(1,i+1):
            print(j,end=" ")

        # Right
        for j in range(i-1,0,-1):
            print(j,end=" ")

        print()

# palindrome_pyramid(5)


# Alphabet Pattern
def alphabet_pyramid(n):
    alphabet = 65
    for i in range(0,n):
        print(" " * (n-i),end="")
        for j in range(0,i+1):
            print(chr(alphabet + i),end=" ")

        print()


# alphabet_pyramid(3)

# Alphabet Triangle 
def alphabet_triangle(n):
    for i in range(0,n):
        alphabet = 65
        for j in range(0,i+1):
            print(chr(alphabet + j),end=" ")

        print()

# alphabet_triangle(5)


# Butterfly Star Pattern
def star_butterfly(n):
    # top
    for i in range(1,n+1):
        # top left
        for j in range(0,i):
            print("*",end="")

        # top right
        print((" " * 2*(n-i)),end="")
        for j in range(0,i):
            print("*",end="")

        print()

    
    # Bottom
    for i in range(n,0,-1):
        # bottom left
        for j in range(0,i):
            print("*",end="")

        # bottom right
        print(" " * (2*(n-i)),end="")
        for j in range(0,i):
            print("*",end="")

        print()


# star_butterfly(7)

# Getting and Validating n
def get_and_validate_n():
    while True:
        try:
            n = int(input("Enter n(size): "))
    
            if n <= 0:
                raise ValueError("value must be positive integer")
            break
                    
        except ValueError as error:
            print(f"Invalid Input, size must be positive integer")
    return n

# Menu Driven

def main():
    print("="*80)
    print("Select a pattern to print")
    print("-"*80)
    print("Enter 1 for star_triangle pattern")

    print("Enter 2 for reverse_star_triangle pattern")

    print("Enter 3 for star_pyramid pattern")

    print("Enter 4 for reverse_star_triangle pattern")

    print("Enter 5 for hollow_square pattern (for hollow sqaure value must be minimum 3)")

    print("Enter 6 for diamond pattern")

    print("Enter 7 for pascal_triangle pattern")

    print("Enter 8 for flody_triangle pattern")

    print("Enter 9 for palindrome_pyramid pattern")

    print("Enter 10 for alphabet_pyramid pattern")

    print("Enter 11 for alphabet_triangle pattern")

    print("Enter 12 forstar_butterfly pattern")

    print("Enter 999 for exit")

    print("="*80)

    while True:

        while True:
            try:
                pattern_choice = int(input("Enter Choice Number: "))

                if pattern_choice not in np.arange(1,13) and pattern_choice != 999:
                    raise ValueError("pattern choice number should be same as instructed")

                break

            except ValueError as error:
                print("Invalid Input, pattern choice number should be interger as instructed.")



        # case
        
        print("="*80)
        match pattern_choice:
            case 1:
                n = get_and_validate_n()
                star_triangle(n)

            case 2:
                n = get_and_validate_n()
                reverse_star_triangle(n)

            case 3:
                n = get_and_validate_n()
                star_pyramid(n)

            case 4:
                n = get_and_validate_n()
                reverse_star_pyramid(n)

            case 5:
                while True:
                    n = get_and_validate_n()

                    if n >= 3:
                        break
                    else:
                        print("Value must be atleast 3 for hollow sqaure")

                hollow_square(n)

            case 6:
                while True:
                    n = get_and_validate_n()

                    if n >= 3 and n%2 != 0:
                        break
                    else:
                        print("Value for diamond must be odd and greater than or equal to 3")

                diamond(n)

            case 7:
                n = get_and_validate_n()
                pascal_triangle(n)

            case 8:
                n = get_and_validate_n()
                flody_triangle(n)

            case 9:
                n = get_and_validate_n()
                palindrome_pyramid(n)

            case 10:
                while True:
                    n = get_and_validate_n()

                    if n <= 26:
                        break
                    else:
                        print("Note: There are only 26 alphabets. So, value should less than 27")
                alphabet_pyramid(n)

            case 11:
                while True:
                                    n = get_and_validate_n()
                
                                    if n <= 26:
                                        break
                                    else:
                                        print("Note: There are only 26 alphabets. So, value should less than 27")
                alphabet_triangle(n)

            case 12:
                while True:
                    n = get_and_validate_n()

                    if n >= 2:
                        break
                    else:
                        print("Value must be atleast 2")

                star_butterfly(n)

            case 999:
                return 1

        print("="*80)




if __name__ == "__main__":
    main()