# Calculator Package

## Technologies

* [Python 3.9](https://python.org) : Base programming language for development. The latest version of python.
* [Docker Engine and Docker Compose](https://www.docker.com/) : Containerization of the application and services orchestration

## Description
This package just contains implementation of a simple Calculator that can do basic addition, subtraction, multiplication, division and nth root calculation.
Like most other calculators, this calculator can be reset and cleared of all previous calculation history with the reset method.

## Getting Started

Using this package is very simple, all you need is to have Git and Docker Engine installed on your machine. 
cd into your project, then open up your terminal and run this command `pip install git+https://github.com/Rafiatu/calculator` to install the package and you're good to go!

The calculator can then be imported thus: `from calculator import Calculator`

Calculator contains 6 methods which are add(), subtract(), multiply(), divide(), root(), and reset_memory(). 
The first 4 are self explantory and take in the number to be calculated by.
root() takes in the desired root number. reset_memory() takes in no arguments and is used to clear the calculator history and reset the value to 0

Example:
```
    from calculator import Calculator
    calculator = Calculator()
    calculator.add(20)
    calculator.subtract(5)
    calculator.divide(3)
    calculator.multiply(5)
    calculator.root(2) -> 5
    calculate.reset_memory() -> 0
```

## Testing


This package has pytest embedded in it and can be run with the following command `python -m pytest tests/` from the root folder


## License

The MIT License - Copyright (c) 2021 - Rafihatu Bello
