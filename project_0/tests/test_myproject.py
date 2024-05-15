from project_0 import main

def test_function1():
    r : str = main.my_first_function()
    assert r == "Hello World!"

def test_function2():
    r : str = main.my_first_function()
    assert r != "Pakistan"