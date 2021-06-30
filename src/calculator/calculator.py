class Calculator:
    '''
        This is a simple Calculator that performs basic addition, subtraction,
        division, multiplication and root calculation of numbers.
    '''
    def __init__(self):
        self.val = 0

    def add(self, num):
        # add a number to the current value in the calculator
        self.val += num
        return self.val

    def subtract(self, num):
        # subtract a number from the current value in the calculator
        self.val -= num
        return self.val

    def multiply(self, num):
        # multiply a number with the current value in the calculator
        self.val *= num
        return self.val

    def divide(self, num):
        # divides the current value in the calculator by the given number
        try:
            self.val /= num
            return self.val
        except ZeroDivisionError:
            return f'{num} cannot be divided by zero'

    def root(self, n):
        # gets the n root of the current value in the calculator
        self.val **= (1/n)
        return self.val

    def reset_memory(self):
        # clears all calculator history and resets the value to zero.
        self.val = 0
        return self.val
