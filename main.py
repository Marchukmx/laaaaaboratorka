import logging

class Calculator:
    def __init__(self):
        self.logger = logging.getLogger("Calculator")
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())

    def add(self,a,b):
        result = a + b
        self.logger.info(f" {a} + {b} = {result}")
        return result
    def minus(self,a,b):
        result = a - b
        self.logger.info(f" {a} - {b} = {result}")
        return result
    def multiply(self,a,b):
        result = a * b
        self.logger.info(f" {a} * {b} = {result}")
        return result
    def devine(self,a,b):
        if b!=0:
            result = a / b
            self.logger.info(f" {a} / {b} = {result}")
            return result
        else:
            raise ValueError("Помилка! Ділення на 0 ")

calculator1 = Calculator()
calculator1.add(1,6)
calculator1.minus(66,22)
calculator1.multiply(50,2)
calculator1.devine(800000,400000)