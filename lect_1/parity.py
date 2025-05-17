def main():
    x = int (input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

#We can notice that 0 is the value of a false statement. Since we have to check if x%2 is equal to 0,
#we can also implement it with this method
def is_even(x):
#   return not x%2
    return True if x % 2 == 0 else False
main()