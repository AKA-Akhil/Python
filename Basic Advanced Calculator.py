import math

class Cal:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

class TrigoCal(Cal):
    def sin(self, angle):
        return math.sin(math.radians(angle))

    def cos(self, angle):
        return math.cos(math.radians(angle))

    def tan(self, angle):
        if math.cos(math.radians(angle)) == 0:
            raise ValueError("Tan is undefined for the given angle.")
        return math.tan(math.radians(angle))

def main():
    try:
        calc = TrigoCal()

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
        operation = input("Select operation (1-4): ")

        if operation not in {'1', '2', '3', '4'}:
            raise ValueError("Invalid operation selected.")

        if operation == '4':
            result = calc.div(num1, num2)
        elif operation == '3':
            result = calc.mul(num1, num2)
        elif operation == '2':
            result = calc.sub(num1, num2)
        else:
            result = calc.add(num1, num2)

        print(f"Result: {result}")

        angle = float(input("Enter an angle for trigonometric functions: "))
        print(f"Sin({angle}): {calc.sin(angle)}")
        print(f"Cos({angle}): {calc.cos(angle)}")   
        print(f"Tan({angle}): {calc.tan(angle)}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
