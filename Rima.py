def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0: return "Error: Division by zero!"
    return x / y

def calculator():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    print("--- Simple Python Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op in operations:
            result = operations[op](num1, num2)
            print(f"\nResult: {num1} {op} {num2} = {result}")
        else:
            print("Invalid operation!")
            
    except ValueError:
        print("Invalid input! Please enter numbers.")

if __name__ == "__main__":
    calculator()