def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation():
    while True:
        op = input("Enter an operation (+, -, *, /): ").strip()
        if op in ('+', '-', '*', '/'):
            return op
        print("Invalid operation. Please enter one of +, -, *, /.")

def perform_calculation(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            return "Error: Division by zero."
        return num1 / num2

def calculator():
    while True:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        op = get_operation()
        
        result = perform_calculation(num1, num2, op)
        print(f"The result is: {result}")

        again = input("Do you want to perform another calculation? (yes/exit): ").strip().lower()
        if again != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

if __name__ == "__main__":
    calculator()
