import pytest
from template_workshop import Fibonacci

def test_import():
    # This checks __init__ was set up correctly
    try:
        from template_workshop import Fibonacci
    except ImportError:
        assert False

##### YOUR CODE HERE #####
def test_consistency():
    fib1 = Fibonacci()
    fib2 = Fibonacci()

    assert fib1.fib(10) == fib2.fib(10)

def test_special_cases():
    fib = Fibonacci()
    assert fib.fib(0) == 0
    assert fib.fib(1) == 1
    assert fib.fib(2) == 1

def test_sequence():
    fib = Fibonacci()
    assert fib.fib(3) == 2
    assert fib.fib(10) == 55
##########################