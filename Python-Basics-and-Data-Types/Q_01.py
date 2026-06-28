# Swap two variables without using a third variable.

a = 2
b = 3

def swap_variables(a,b):
    return b,a

a,b = swap_variables(2,3)

print("a: ",a)
print("b: ",b)