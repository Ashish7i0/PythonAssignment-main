from getpass import getpass

def check_password_strength(password):
    # Checking minimum length of the user input password
    if len(password) < 8:
        return False
    
    # Checking presence of any uppercase and any lowercase letter
    has_uppercase_letter = any(c.isupper() for c in password)
    has_lowercase_letter = any(c.islower() for c in password)
    if not (has_uppercase_letter and has_lowercase_letter):
        return False
    
    # Checking presence of at least one digit
    has_digit = any(c.isdigit() for c in password)
    if not has_digit:
        return False

    # Checking presence of at least one special character
    special_characters = "~`!@#$%^&*()_-+{}[]|:;'<,>"
    has_special = any(c in special_characters for c in password)
    if not has_special:
        return False
    
    # All of the above conditions for a strong password are met
    return True

# Get user input 
# Using getpass function, to ensure the entered password is not displayed in the screen for better security
user_password = getpass("Enter any password you would like to check the strength: ")

# Validate the strength of the password
if check_password_strength(user_password):
    print("The password you have entered is strong!")
else:
    print("The password you have entered does not meet the criteria. Please choose a different password.")
