import re

#Validate a user's email address
email=input("What's your email? ").strip()

#if "@" in email and "." in email: 
#    print("Valid")
#else:
#    print("Invalid")
#-----------------------------------------------------
#username, domain = email.split("@")
#
#if username and domain.endswith(".edu"): 
## if username: -> Checks whether the username exists or is equal to ""
#    print("Valid")
#else:
#    print("Invalid")
#-----------------------------------------------------
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
#\. -> Literally a dot
#      Necessary to type an r before the string
#(\w+\.)? -> To cover the case in which we define a subdomain (cs50.harvard.edu)
#\w = [a-zA-Z0-9_] = every alpha-numeric symbol with underscore included
    print("Valid")
    
else:
    print("Invalid")