def camel_to_snake(variable_name):
    # Initialize an empty string to store the snake case variable name
    snake_case_name = ""

    # Iterate over each character in the variable name
    for i, char in enumerate(variable_name):
        # Check if the current character is uppercase (except for the first character)
        if char.isupper() and i != 0:
            # If the current character is uppercase, insert an underscore before it
            snake_case_name += "_" + char.lower()
        else:
            # Otherwise, append the character as is
            snake_case_name += char.lower()

    return snake_case_name

def main():
    # Prompt the user for the variable name in camel case
    camel_case_name = input("Enter the variable name in camel case: ")

    # Convert the variable name to snake case
    snake_case_name = camel_to_snake(camel_case_name)

    # Output the snake case variable name
    print(f"The snake case variable name is: {snake_case_name}")

if __name__ == "__main__":
    main()