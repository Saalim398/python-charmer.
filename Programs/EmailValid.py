import re

email = input("Enter your email: ")
regex = re.fullmatch("^[a-z][a-z0-9._]+@[a-z]+\.[a-z]{2,3}", email.lower())

print("Valid Email" if regex else "Invalid Email")