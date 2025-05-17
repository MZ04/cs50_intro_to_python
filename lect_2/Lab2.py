"""
for i in range(3):
    print("meow")
#Alternative solution: print("meow\n"*3, end="")
"""
#Check if the input value is positive, else we ask again
"""
while True:
    n = int (input("What's n? "))
    if n > 0:
        break 

for _ in range(n):
    print("meow")
"""
def main():
    number=get_number()
    meow(number)

def get_number():
    while True:
        n=int(input("What's n? "))
        if n>0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()