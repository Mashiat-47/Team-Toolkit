def calculator():
    print("\n===== CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose an operation: ")

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice!")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", num1 + num2)

        elif choice == "2":
            print("Result:", num1 - num2)

        elif choice == "3":
            print("Result:", num1 * num2)

        elif choice == "4":
            if num2 == 0:
                print("Error: Cannot divide by zero!")
            else:
                print("Result:", num1 / num2)

    except ValueError:
        print("Please enter valid numbers.")