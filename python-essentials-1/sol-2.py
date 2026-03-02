try:
    # 1. Take first name and last name as input
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    # 2. Take age as input (as a string initially for error checking)
    age_input = input("Enter your age: ")

    # 4. Age is not numeric → print "Invalid age input" (check before conversion)
    if not age_input.isdigit():
        print("Invalid age input")
    else:
        # 3. Convert the age into an integer
        age = int(age_input)

        # 4. Age is less than 0 → print "Age cannot be negative"
        if age < 0:
            print("Age cannot be negative")
        else:
            # Print Full name using string concatenation
            full_name = "Full Name: " + first_name + " " + last_name
            print(full_name)

            # Print Age next year
            age_next_year = "You will be " + str(age + 1) + " next year"
            print(age_next_year)

except ValueError:
    # This might catch unexpected non-numeric inputs if the isdigit check was removed,
    # but the current structure handles it gracefully within the if not age_input.isdigit(): block.
    pass