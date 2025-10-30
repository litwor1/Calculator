from typing import Optional

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

    def divide(self) -> Optional[float]:
        if self.__op2 == 0:
            return None
        return self.__op1 / self.__op2
