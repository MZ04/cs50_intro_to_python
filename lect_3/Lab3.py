def main():
    x=get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
#prompt = the message the user will see
    while True:
        try:
            return int(input(prompt))
            #break -> It would be okay, since the exception is detected at the line above
        except ValueError:
            print("x is not an integer")
main()