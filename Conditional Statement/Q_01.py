# A company has a predefined username and password. Write a Python program to validate the user's login credentials.

# Stored Credentials

# Username : admin
# Password : admin123

def user_credentials():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    return username, password

def validate_user_credentials(username,password):

    if not username:
        return False,"Username is empty!"
    
    if not password:
        return False,"Password is empty!"
    
    if username.lower() != "admin" and password != "admin123":
        return False,"Invalid Username & Password"
    
    if username.lower() != "admin":
        return False,"Invalid Username"
    
    if password != "admin123":
        return False,"Invalid Password"
    
    return True
    
def main():
    username, password = user_credentials()

    isvalid,messg=validate_user_credentials(username,password)

    if isvalid:
        return f"Login Successful\nWelcome admin!"
    else:
        return messg

print(main())