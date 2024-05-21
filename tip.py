def calculate_tip(total_amount, tip_percentage):
    """
    Calculate the tip amount given the total bill and tip percentage.
    """
    tip_amount = total_amount * (tip_percentage / 100)
    return tip_amount

def main():
    total_amount = float(input("Enter the total amount of the bill: $"))

    # Checking if the total amount is valid
    if total_amount <= 0:
        print("Invalid total amount. Please enter a positive value.")
        return

    # Asking for tip percentage until a valid one is provided
    while True:
        tip_percentage = float(input("Enter the tip percentage (15%, 20%, etc.): "))
        if tip_percentage >= 0:
            break
        print("Invalid tip percentage. Please enter a non-negative value.")

    tip_amount = calculate_tip(total_amount, tip_percentage)
    print(f"Tip Amount: ${tip_amount:.2f}")

if __name__ == "__main__":
    main()