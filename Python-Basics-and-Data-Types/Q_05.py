# Convert Fahrenheit to Celsius.
# Formula:
# C = (F - 32) * 5/9


def fahrenheit_to_celsius(fahrenheit):
    """
        Convert temperature from Fahrenheit to Celsius.
    """

    return round((fahrenheit - 32) * 5/9,2)

print(fahrenheit_to_celsius(32))