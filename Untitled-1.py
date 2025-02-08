def hex_to_decimal(hex_str):
    try:
        decimal = int(hex_str, 16)
        return decimal
    except ValueError:
        return "Invalid hexadecimal input!"

def decimal_to_hex(decimal_num):
    try:
        hex_str = hex(int(decimal_num))
        return hex_str
    except ValueError:
        return "Invalid decimal input!"

def main():
    print("Hexadecimal to Decimal and Decimal to Hexadecimal Converter")
    print("1. Hexadecimal to Decimal")
    print("2. Decimal to Hexadecimal")
    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        hex_input = input("Enter a hexadecimal number: ").strip()
        result = hex_to_decimal(hex_input)
        print(f"Decimal: {result}")
    elif choice == '2':
        decimal_input = input("Enter a decimal number: ").strip()
        result = decimal_to_hex(decimal_input)
        print(f"Hexadecimal: {result}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
