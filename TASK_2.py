print("\n**********| SIMPLE CALCULATOR |**********")
while True:
    print("""\n----------|MAIN MENU|----------
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exit""")
    try:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        choice = int(input("\nEnter your choice (1/2/3/4/5): "))

        if choice == 1:
            add = num1 + num2
            print(f"\nRESULT: {num1} + {num2} = {add}")
        elif choice == 2:
            if num1 > num2:
                sub = num1 - num2
                print(f"\nRESULT: {num1} - {num2} = {sub}")
            else:
                sub = num2 - num1
                print(f"\nRESULT: {num2} - {num1} = {sub}")
        elif choice == 3:
            multiply = num1 * num2
            print(f"\nRESULT: {num1} x {num2} = {multiply}")
        elif choice == 4:
            if num2 == 0:
                raise ZeroDivisionError("\nCannot divide by zero.")
            divide = num1 / num2
            print(f"\nRESULT: {num1} / {num2} = {round(divide,3)}")
        elif choice == 5:
            exit()
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")
    except ZeroDivisionError as e:
        print(e)
