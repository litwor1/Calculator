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
        if self.__op2 == 0:
            raise ZeroDivisionError("Error: Division by zero!")
        return self.__op1 / self.__op2

#
# if __name__ == "__main__":
#     c = Calculator(2, 3)
#     print(f"c.sum: {c.sum()}")
#     print(f"c.subtract: {c.subtract()}")
#     print(f"c.multiply: {c.multiply()}")
#     print(f"c.divide: {c.divide()}")
#
#     c = Calculator(2, 0)
#     print(f"c.sum: {c.sum()}")
#     print(f"c.subtract: {c.subtract()}")
#     print(f"c.multiply: {c.multiply()}")
#     try:
#         print(f"c.divide: {c.divide()}")
#     except ZeroDivisionError:
#         print("Division by zero is forbidden!")
