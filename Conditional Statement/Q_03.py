# A healthcare system needs to classify a person's Body Mass Index (BMI).
# Write a Python program that calculates BMI and displays the appropriate health category.

# BMI Formula

# BMI = Weight(kg) / ((height (m))**2)

# BMI Categories

# | BMI            | Category      |
# | -------------- | ------------- |
# | Less than 18.5 | Underweight   |
# | 18.5 – 24.9    | Normal Weight |
# | 25.0 – 29.9    | Overweight    |
# | 30.0 or above  | Obese         |


def get_user_weight_height():
    weight = input("Enter Weight (Kg): ")
    height = input("Enter Height (m): ")

    return weight,height

def cal_BMI(weight,height):

    if any(x <= 0 for x in (weight,height)):
        raise ValueError("Weight & Height must be non-negative and non-zero integer")

    bmi = (weight / (height**2))

    return bmi

def BMI_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi >= 18.5 and bmi <= 24.9:
        return "Normal Weight"
    
    elif bmi >= 25 and bmi <= 29.9:
        return "Overweight"

    else:
        return "Obese"

def main():
    weight, height = get_user_weight_height()

    try:
        weight = float(weight)
        height = float(height)
    except ValueError:
        return "Weight & Height must be non-negative interger"

    bmi = cal_BMI(weight,height)
    bmi_cat = BMI_category(bmi)

    return f"""
BMI: {bmi}
Category: {bmi_cat}
"""


if __name__ == "__main__":
    print(main())