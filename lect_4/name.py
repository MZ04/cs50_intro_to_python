import sys 


#while True:
#    try:
#        print ("Hello, my name is", sys.argv[1])
#        break
#    except IndexError: #To handle the case in which is typed no name
#        print("You inserted no name!")
#        sys.argv.append(input("Insert the name: "))
#I suppose than, given that the first argument is the name of the file, 
# the second argument is going to be the name


#ALTERNATIVE SOLUTION
#Check for errors
if len(sys.argv)<2:
    sys.exit("Too few arguments")

#Print variable lines where we greet different names
#If we type for arg in sys.argv: even "Hello, my name is name.py" is going to appear
#A "slice" of the list is needed
for arg in sys.argv[1:-1]: 
#With "1:" I'm specifying the start of the iteration, not the end
    print("Hello, my name is", arg)
#Since sys.argv is a list we can use the functions implemented for the lists