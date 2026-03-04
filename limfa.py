def power(base, exponent):
    return base ** exponent  


def main():
    print("=== Power Calculator ===")
    try:
        
        base = float(input("Enter the base number: "))
        exponent = float(input("Enter the exponent: "))

       
        result = power(base, exponent)

    
        print(f"{base} raised to the power of {exponent} is: {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values only.")


if __name__ == "__main__":
    main()