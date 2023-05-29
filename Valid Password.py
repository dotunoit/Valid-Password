import re

def new_password(password):
    try:
        if len(password) < 6:
            print("Password is too short! minimum length of transaction password: 6")
            return False
        if len(password) > 12:
            print("Password is too long! maximum length of transaction password is 12")
            return False    
        
        lowercase = re.search("[a-z]", password)
        uppercase = re.search("[A-Z]", password)
        digit = re.search("[0-9]", password)
        symbol = re.search("[$#@]", password)
        
        if not lowercase:
            print("Password must contain at least 1 lowercase letter")
        
        if not uppercase:
            print("Password must contain at least 1 uppercase letter")
        
        if not digit:
            print("Password must contain at least 1 digit")
        
        if not symbol:
            print("Password must contain at least 1 character from [$#@]")
        
        if not (lowercase and uppercase and digit and symbol):
            return False
        
        return True
    
    except TypeError:
        return False

print("Kindly enter a new password for your account")
print("P.S. Your password must contain the following:")
print("1. At least 1 letter between [a-z]")
print("2. At least 1 number between [0-9]")
print("3. At least 1 letter between [A-Z]")
print("4. At least 1 character from [$#@]")
print("5. Minimum length of transaction password: 6")
print("6. Maximum length of transaction password: 12")

# Test the password validity
password = input("Enter the password: ")
if new_password(password):
    print("Password is valid.")
else:
    print(f"The password '{password}' is invalid.")
