# Create a function that takes email address as input in the following format:
# firstName.lastName@exam.com
# and returns a string that represents the user name in the following format:
# last_name first_name
# example: "elek.viz@exam.com" for this input the output should be: "Viz Elek"
# accents does not matter

# print(name_from_email("elek.viz@exam.com"))

user_email = input("Please enter an email-address: ")

def name_from_email(email):
    name = user_email.split("@")
    first_last = name[0].split(".")
    return first_last[1].capitalize() + " " + first_last[0].capitalize()

print(name_from_email(user_email))
