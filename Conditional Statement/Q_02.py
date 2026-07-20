# A government system needs to determine whether a citizen is eligible to vote.
# Write a Python program that checks a person's voting eligibility based on their age.

# Rules
# Age must be a valid integer.
# Age cannot be negative.
# A person is eligible to vote if Age ≥ 18.

def get_age():
    age = input("Enter Age: ")

    return age

def voting_eligibility(age: int) -> tuple[bool,str]:
    if not isinstance(age,int):
        raise TypeError("Age must be positive integer")
    
    if age < 0:
        raise ValueError("Age must be non-negative")
    
    if age == 0:
        raise ValueError("Age must be non-zero")
    
    if age >= 18:
        return True,"Eligible to vote"
    return False,"Not Eligible to vote"


def main():
    age = get_age()

    try:
        age = int(age)
    except ValueError:
        return "Age must be non-negative integer"

    is_eligible,messg = voting_eligibility(age)

    if is_eligible:
        return messg
    else:
        return f"""
{messg}
You can vote after {18-age} years
"""
    
if __name__ == "__main__":
    print(main())