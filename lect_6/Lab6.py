#names = []
#
#for _ in range(3):
#    names.append(input("What's your name? "))
#
#
#sorted: returns a sorted version of that list
#for i in sorted(names):
#    print(f"hello, {i}")

#name = input("What's your name? ")
#
#with open("names.txt", "a") as file:
#    file.write(name+"\n")

#with open("names.txt", "r") as file:
#    lines=file.readlines()
#
#for line in lines:
#    print("hello,", line, end="")

#with open("names.txt", "r") as file:
#    for line in file:
#    Python automatically associates the line variable to a single line of the file
#        print("hello,", line.rstrip())

#names = []
#with open("names.txt") as file:
#    for line in file:
#        names.append(line.rstrip())
#
#for name in sorted(names):
#    print(f"hello, {name}")

with open("names.txt") as file:
    for line in sorted(file):
        print(f"hello, {line.rstrip()}")