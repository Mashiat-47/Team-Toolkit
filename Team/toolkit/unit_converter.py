def unit_converter():
    print("\n===== UNIT CONVERTER =====")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")

    choice = input("Choose a conversion: ")

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice!")
        return

    try:
        value = float(input("Enter the value: "))

        if choice == "1":
            print("Result:", value * 0.621371, "miles")
        elif choice == "2":
            print("Result:", value / 0.621371, "kilometers")
        elif choice == "3":
            print("Result:", (value * 9/5) + 32, "°F")
        elif choice == "4":
            print("Result:", (value - 32) * 5/9, "°C")

    except ValueError:
        print("Please enter a valid number.")