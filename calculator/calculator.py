def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


# Perform a calculation directly
num1 = 10
num2 = 5
operation = 'add'

if operation == 'add':
    result = add(num1, num2)
elif operation == 'subtract':
    result = subtract(num1, num2)
elif operation == 'multiply':
    result = multiply(num1, num2)
elif operation == 'divide':
    result = divide(num1, num2)
else:
    result = "Invalid operation"

print(f"{num1} + {num2} = {result}")