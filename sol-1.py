try:
    num1_str = input("Enter the first number: ")
    num2_str = input("Enter the second number: ")
    num1 = int(num1_str)
    num2 = int(num2_str)
   
    sum_result = num1 + num2
    print(f"Their sum: {sum_result}")

    # Calculate division with ZeroDivisionError handling
    try:
        division_result = num1 / num2
        print(f"Their division result: {division_result}")
    except ZeroDivisionError:
        print("Cannot divide by zero") 

except ValueError:
    print("Invalid input")