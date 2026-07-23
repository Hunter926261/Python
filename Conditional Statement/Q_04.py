# A company's registration system needs to check whether a user's password is strong enough.

# Write a Python program to classify the password strength.

# Password Rules

# A password is considered Strong if it:

# Has at least 8 characters
# Contains at least one uppercase letter
# Contains at least one lowercase letter
# Contains at least one digit
# Contains at least one special character
# (@ # $ % & * ! ?)

def get_password():
    password = input("Enter Password: ")

    return password

def check_password_strength(password):
    password = password.strip()

    # min. length must be 8
    if len(password) < 8:
        return False, "Password is too Short"
    
    # Contains at least one uppercase letter
    if not any(x.isupper() for x in password):
        return False, "Password must contain upper case"
    
    # Contains at least one lowercase letter
    if not any(x.islower() for x in password):
        return False, "Password must contain lower case"
    
    # Contains at least one digit
    if not any(x.isdigit() for x in password):
        return False,"Password must contain numbers"
    
    # Contains at least one special character (@ # $ % & * ! ?)
    if not any(x in "@#$%&*!?" for x in password):
        return False, "Password must contain special character"
    
    return True,"Password Generated Successfully..."

def main():
    password = get_password()

    if not isinstance(password,str):
        raise "Password must be string"

    is_strong, messg = check_password_strength(password)

    if is_strong:
        return messg
    else:
        return f"""
Not Strong password Try Again
{messg}
"""

if __name__ == "__main__":
    print(main())