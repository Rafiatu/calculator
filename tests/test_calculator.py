from src.calculator_package.calculator import Calculator


calc = Calculator()
def test_adds_number():
    assert calc.add(5) == 5

def test_subtracts_number():
    assert calc.subtract(3) == 2

def test_multiplies_number():
    assert calc.multiply(10) == 20

def test_divides_number():
    assert calc.divide(5) == 4

def test_nth_root():
    assert calc.root(2) == 2

def test_reset_calculator():
    assert calc.reset_memory() == 0