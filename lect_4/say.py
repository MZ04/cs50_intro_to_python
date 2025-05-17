import sys 

from sayings import hello 
#When we say to import the function "hello", the program reads from top to bottom
#the entire "sayings" file. Thus, it reads the "main" function's call as well and then executes it 

if len(sys.argv)==2:
    hello(sys.argv[1])
