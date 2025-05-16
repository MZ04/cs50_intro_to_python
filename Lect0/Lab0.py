"""
#Reads the string in input
name = input("What's your name? ")

#If a lot of white spaces are in the string before the name, they need to be removed
name=name.strip()

#To capitalize the user's input (it works just with the first word)
name=name.capitalize()

#To use the title format for the user's input (it capitalizes every word in the string)
name=name.title()

#We can do everything at the same time
name=name.strip().capitalize().title()

#We can link with the input directly
name = input("What's your name? ").strip().capitalize().title()

#Split user's name into first name and last name
first, last = name.split(" ")
print(f"hello, {first}")
"""
def main():
    name= input("What's your name? ")
    hello(name)
    hello()

def hello(name="world"):
    print("Hello " + name )


main()