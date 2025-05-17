def hello(name):
    print(f"Hello, {name}")


def goodbye(name):
    print(f"Goodbye, {name}") 

def main():
    hello("world")
    goodbye("world")
if __name__ == "__main__":
    main()
#With this condition we prevent to run main if it is used as a module to other programs