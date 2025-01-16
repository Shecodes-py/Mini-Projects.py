import re

address1 = "hackerRank@coding.com.Uk"
address2 = "leetcodeis fun-ish 123"
address3 = "geeksforgeeks@coding"
address4 = "cognizify@internship.com"
address5 = "username.com@gmail"
user_input = input("Enter an Email: ")
validation = [address1, address2, address3, address4, address5, user_input]

email_pattern = r"^[a-zA-Z0-9.]+@[a-zA-Z]+\.[a-z]{2,}+(\.[a-zA-Z]+)?$"
for email in validation:
    if re.match(email_pattern, email):
        print(f"{email} is a valid email address")
    else:
        print(f"{email} is not a valid email address")

