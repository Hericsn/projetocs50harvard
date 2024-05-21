def main():
    # Prompt the user for an arithmetic expression
    expression = input("Enter an arithmetic expression (e.g., 1 + 1): ")

    # Split the input into components
    x, operator, z = expression.split()

    # Convert the operands to integers
    x = int(x)
    z = int(z)

    # Perform the arithmetic operation based on the operator
    if operator == '+':
        result = x + z
    elif operator == '-':
        result = x - z
    elif operator == '*':
        result = x * z
    elif operator == '/':
        result = x / z
    else:
        raise ValueError("Invalid operator. Operator must be +, -, *, or /.")

    # Output the result formatted to one decimal place
    print(f"{result:.1f}")

if __name__ == "__main__":
    main()