from src.calculator import Calculator
from src.calculator.calculator import CalculatorException
import pytest


def test_adds_number_correctly():
    calc = Calculator()
    assert calc.add(5) == 5


def test_subtracts_number_correctly():
    calc = Calculator()
    assert calc.subtract(3) == -3


def test_multiplies_number_correctly():
    calc = Calculator()
    calc.add(10)
    assert calc.multiply(10) == 100


def test_divides_number_correctly():
    calc = Calculator()
    calc.add(20)
    assert calc.divide(5) == 4


def divide_by_zero():
    calc = Calculator()
    calc.add(13)
    calc.divide(0)


def test_does_not_divide_by_zero():
    with pytest.raises(CalculatorException,
                       match=r"Something went wrong."):
        divide_by_zero()


def test_gets_correct_nth_root():
    calc = Calculator()
    calc.add(16)
    assert calc.root(2) == 4


def zeroth_root():
    calc = Calculator()
    calc.add(25)
    calc.root(0)


def test_raises_exception_for_zeroth_root():
    with pytest.raises(CalculatorException,
                       match=r"Something went wrong."):
        zeroth_root()


def test_resets_calculator_properly():
    calc = Calculator()
    assert calc.reset_memory() == 0


def add_string_input():
    calc = Calculator()
    calc.add("Rafi")


def test_handles_wrong_input_with_add_function():
    with pytest.raises(CalculatorException,
                       match=r"Something went wrong."):
        add_string_input()


def test_adds_float_input_correctly():
    calc = Calculator()
    calc.add(17.5)


def test_subtracts_float_input_correctly():
    calc = Calculator()
    calc.add(30)
    assert calc.subtract(15.7) == 14.3


def test_divides_float_input_correctly():
    calc = Calculator()
    calc.add(14)
    assert calc.divide(3.5) == 4


def test_multiplies_float_correctly():
    calc = Calculator()
    assert calc.multiply(17.5) == 0
