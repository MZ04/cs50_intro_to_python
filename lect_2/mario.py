def print_column(height):
    for _ in range(height):
        print("#")

def main():
    print_square(3)

def print_row(width):
    for _ in range(width):
        print("?"*4)

def print_square(size):
    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
    """
    for _ in range(size):
        print("#"*size)
    
    or
     
    for _in range(size):
        print_row(size)"""

main()