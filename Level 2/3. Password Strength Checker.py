# Password Strength Checker
import re

password_strength = False
feedback = '''--------Password Criteria--------\n1. Password should be at least 8 characters long\n2. Include both UPPERCASE and lowercase letters.\n3. Add at least one special character.\n4. Password must include digits.'''
print(feedback)

while password_strength == False:
    password = input("Enter your password to chek it's strength: ")
    strength = r"^[A-z](?=.*\w)(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

    if " " in password:
        print("Ensure there are no spaces in your password")
    else:
        if len(password) > 8:
            if re.match(r"^[A-Z]", password):
                if re.match(r"?=.*\d", password):
                    if re.match(strength, password):
                        print("Your Password is solid ✅")
                        password_strength = True
                    else:
                        print("Your password is not strong enough")
                else:
                    print("Password must contain digits")
            else:
                print("Password must begin with an Uppercase letter")
        else:
            print("Password must be greater than 8 characters")

