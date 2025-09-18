from validate_email_address import validate_email

# Take email input from user
email = input("Enter email: ")

# Validate email
is_valid = validate_email(email, verify=False)  # verify=False means no email will be sent

if is_valid:
    print(f"{email} is a valid email format.")
else:
    print(f"{email} is NOT a valid email format.")
