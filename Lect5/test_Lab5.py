#File created with the sole purpose of testing the "Lab5.py" program
#Conventions -> The file is called "test_<file>", referred to the file we want to test 
from Lab5 import square
import pytest

#Convention -> The function is called test_<function>, referred to the function that this function wants to test
#To test a program we need to test some corner cases -> Corner cases are found just by instinct, 
#                                                         there are no methods
#def test_square():
    #try:
    #    assert square(2) == 4
    #except:
    #    print("2 squared was not 4")
    #try:
    #    assert square(3) == 9
    #except:
    #    print("3 squared was not 9")
    #try:
    #    assert square(-2) == 4
    #except:
    #    print("-2 squared was not 4")
    #try:
    #    assert square(-3) == 9
    #except:
    #    print("-3 squared was not 9")
    #try:
    #    assert square(0) == 0
    #except:
    #    print("0 squared was not 0")
    #Various prints and try-except handled automatically by pytest

#We can separate the test into smaller categories to check how many error do we have
def test_positive():
    assert square(2)==4
    assert square(3)==9
    
    
def test_negative():
    assert square(-2)==4
    assert square(-3)==9


def test_0():
    assert square(0)==0

def test_str():
#We expect that, if we pass a string to the square function, it's going to raise an error
    with pytest.raises(TypeError):
        square("cat")