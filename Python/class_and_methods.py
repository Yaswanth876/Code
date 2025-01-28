class Calculator:
    def add (self, num1, num2):
        return num1 + num2
if __name__ == "__main__":
    calc = Calculator()
    result = calc.add(20,8)
    print(f"The Sum is {result}")