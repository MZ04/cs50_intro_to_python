def main():
    name= input("What's your name? ")
    print(hello(name))

#def hello(name="world"):
#    print("Hello " + name )

def hello(name="world"):
    return "Hello "+name


if __name__=="__main__":
    main()