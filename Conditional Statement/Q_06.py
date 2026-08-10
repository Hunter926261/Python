# Problem Statement

# A company wants to determine whether an employee is eligible for promotion based on:

# Years of experience
# Performance rating
# Attendance percentage
# Rules

# An employee is eligible for promotion if all conditions are satisfied:

# Experience ≥ 3 years
# Performance rating ≥ 4.0 out of 5
# Attendance ≥ 90%

# Otherwise, the employee is not eligible.

# Input

# Employee Name
# Years of Experience
# Performance Rating
# Attendance Percentage

# Example 1

# Employee Name: Rahul
# Experience: 5
# Performance Rating: 4.5
# Attendance: 95

# Output:
# Employee is eligible for promotion.

# Example 2

# Employee Name: Amit
# Experience: 4
# Performance Rating: 3.5
# Attendance: 95

# Output:
# Employee is not eligible for promotion.
# Reason: Performance rating must be at least 4.0.

# Get Employee Information
def get_employee_details():

    employee_name = ((input("Enter Employee Name: ")).strip())

    if not employee_name:
        raise ValueError("Employee name can not be empty")

    try:
        year_experience = int(input("Enter Year of Experience: "))
    except ValueError:
        raise ValueError("Year of Experience must be in integer")

    try:
        performance_rating = float(input("Enter Performance Rating(Out of 5.0): "))
    except ValueError:
        raise ValueError("Rating must be float or integer between 0-5")

    try:
        attendance_percentage = int(input("Enter Attendance Percentage(ex, 87): "))
    except ValueError:
        raise ValueError("Attendance must be integer between 0-100")

    return employee_name,year_experience,performance_rating,attendance_percentage

def promotion_eligibility(experience,rating,attendance):

    if not isinstance(experience,int):
        raise TypeError("Experience must be in integer")

    if experience < 0:
        raise ValueError("Experience must be non-negative.")

    if not isinstance(rating,(int,float)):
        raise TypeError("Rating must be float(ex, 4.2 or 4)")

    if rating < 0 or rating > 5:
            raise ValueError("Rating must between 0-5")

    if not isinstance(attendance,int):
        raise TypeError("Attendance must be integer(0-100)")

    if attendance < 0 or attendance > 100:
            raise ValueError("Attendance must be between 0 and 100.")

    is_eligible = True
    reason = []

    if experience < 3:
        is_eligible = False
        reason.append("Experience must be at least 3 years")
    if rating < 4.0:
        is_eligible = False
        reason.append("Performance rating must be at least 4.0.")
    if attendance < 90:
        is_eligible = False
        reason.append("Attendance must be at least 90%")

    return is_eligible,reason

def main():

    try:
        employee_name, year_experience, performance_rating, attendance_percentage = get_employee_details()

        is_eligible_for_promotion,reason = promotion_eligibility(year_experience,performance_rating,attendance_percentage)

        if is_eligible_for_promotion:
            return f"""
{employee_name} is eligible for promotion.
    """
        else:
            return f"""
{employee_name} is not eligible for promotion.
Reason: \n{"\n".join(f"- {r}" for r in reason)}
    """

    except (ValueError,TypeError) as error:
        return f"Error: {error}"

if __name__ == "__main__":
    print(main())