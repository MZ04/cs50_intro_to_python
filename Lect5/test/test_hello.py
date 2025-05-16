from hello import hello
import pytest 

def test_argument():
    assert hello("David") == "Hello David"

def test_default():
    assert hello() == "Hello world"
#To test the hello function we need to change the 
#  function into a one which returns something