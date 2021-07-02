class CalculatorException(Exception):
    pass


class Calculator:
    """
        This is a simple Calculator that performs basic addition, subtraction,
        division, multiplication and root calculation of numbers.
    """

    def __init__(self):
        self.__val = 0

    def add(self, num:int or float or complex):
        """add a number to the current value in the calculator"""
        try:
            self.__val += num
            return self.__val
        except Exception:
            raise CalculatorException("Something went wrong. function add() takes only integers")

    def subtract(self, num:int or float or complex):
        """subtract a number from the current value in the calculator"""
        try:
            self.__val -= num
            return self.__val
        except Exception:
            raise CalculatorException("Something went wrong. Ensure to use the right input types")

    def multiply(self, num:int or float or complex):
        """multiply a number with the current value in the calculator"""
        self.__val *= num
        return self.__val

    def divide(self, num:int or float or complex):
        """divides the current value in the calculator by the given number"""
        try:
            self.__val /= num
            return self.__val
        except ZeroDivisionError:
            raise CalculatorException("Something went wrong. "
                                      "You are most likely attempting a division with 0")

    def root(self, num:int):
        """gets the n root of the current value in the calculator"""
        try:
            self.__val **= (1/num)
            return self.__val
        except Exception:
            raise CalculatorException("Something went wrong. "
                                      "You are most likely attempting a division with 0")

    def reset_memory(self):
        """clears all calculator history and resets the value to zero."""
        self.__val = 0
        return self.__val
