# Swap two variables using a third variable.

a = 2
b = 3

def swap_variables(a,b):
    temp = a
    a = b
    b = temp

    return a,b

a,b = swap_variables(a,b)

print("a: ",a)
print("b: ",b)
