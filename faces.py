# faces.py

def convert_str(input_str):
    """
    Convert :) to 🙂 and :( to 🙁 in the input string.
    All other text remains unchanged.
    """
    input_str = input_str.replace(":)", "🙂")
    input_str = input_str.replace(":(", "🙁")
    return input_str

def input_and_convert():
    """
    Prompt the user for input, call convert_str function,
    and print the result.
    """
    user_input = input("Enter a string: ")
    converted_str = convert_str(user_input)
    print("Converted string:", converted_str)

if __name__ == "__main__":
    input_and_convert()