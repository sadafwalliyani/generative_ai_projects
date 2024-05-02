from project_youtube import main

def test_function():
    r= main.my_first()
    assert r == "hello World"

def test_function2():
    r=main.my_first()
    assert r != "Pakistan"

