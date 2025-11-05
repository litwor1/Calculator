class Calculator:
    def __init__(self, op1: float, op2: float):
        self.__op1 = op1
        self.__op2 = op2

    def sum(self) -> float:
        return self.__op1 + self.__op2

    def subtract(self) -> float:
        return self.__op1 - self.__op2

    def multiply(self) -> float:
        return self.__op1 * self.__op2

    def divide(self) -> float:
        return self.__op1 / self.__op2
