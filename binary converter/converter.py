def binary_to_decimal(binary_str):
    """
    Convert a binary string to its decimal equivalent.
    """
    try:
        decimal = int(binary_str, 2)
        return decimal
    except ValueError:
        return "Invalid."


def decimal_to_binary(decimal_int):
    """
    Convert a decimal integer to its binary equivalent.
    """
    try:
        binary = bin(int(decimal_int)).replace("0b", "")
        return binary
    except ValueError:
        return "Invalid decimal number."


def binary_calculator(bin1, bin2, operation):
    """
    Perform binary calculations (addition, subtraction, multiplication, division).
    """
    try:
        # Convert binary strings to decimal
        dec1 = int(bin1, 2)
        dec2 = int(bin2, 2)

        # Perform the chosen operation
        if operation == "add":
            result = dec1 + dec2
        elif operation == "subtract":
            result = dec1 - dec2
        elif operation == "multiply":
            result = dec1 * dec2
        elif operation == "divide":
            if dec2 == 0:
                return "Division by zero error."
            result = dec1 // dec2
        else:
            return "Invalid operation."

        # Convert the result back to binary
        return decimal_to_binary(result)
    except ValueError:
        return "Invalid binary number."


def main():
    while True:
        print("\nBinary to Decimal and Decimal to Binary Converter with Calculator")
        print("1: Binary to Decimal")
        print("2: Decimal to Binary")
        print("3: Binary Calculator (Addition, Subtraction, Multiplication, Division)")
        print("4: Quit")

        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == '1':
            binary_str = input("Enter a binary number: ")
            result = binary_to_decimal(binary_str)
            print(f"Decimal equivalent: {result}")

        elif choice == '2':
            decimal_str = input("Enter a decimal number: ")
            if decimal_str.isdigit():
                decimal_int = int(decimal_str)
                result = decimal_to_binary(decimal_int)
                print(f"Binary equivalent: {result}")
            else:
                print("Invalid input. Please enter a valid decimal number.")

        elif choice == '3':
            bin1 = input("Enter the first binary number: ")
            bin2 = input("Enter the second binary number: ")
            print("Choose an operation: add, subtract, multiply, divide")
            operation = input("Operation: ")
            result = binary_calculator(bin1, bin2, operation)
            print(f"Binary Calculation Result: {result}")

            # Offer to convert the result
            if result and "error" not in result.lower():
                print("Do you want to convert this result to decimal?")
                print("1: Yes")
                print("2: No, continue")
                conversion_choice = input("Enter your choice: ")

                if conversion_choice == '1':
                    decimal_result = binary_to_decimal(result)
                    print(f"Decimal equivalent of the result: {decimal_result}")
                elif conversion_choice == '2':
                    continue
                else:
                    print("Invalid choice. Returning to the main menu.")

        elif choice == '4':
            print("by")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()