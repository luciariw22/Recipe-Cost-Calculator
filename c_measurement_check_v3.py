def yes_no(question):
    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either yes or no...\n")


def measurement():
    # error message
    error = "Please enter a valid measurement\n"

    while True:
        ingredient_name = input("Enter ingredient name or 'xxx' to exit: ").strip().lower()
        if ingredient_name == "xxx":
            return None

        while True:
            # Ask for the amount needed for the recipe
            response = input(f"Amount of {ingredient_name}?: (e.g., 2kg, 200g, 20mL, "
                             "or enter 'xxx' to finish): ").strip().lower()

            if response == "xxx":
                return None

            # Check the measurement
            if response.endswith('kg'):
                print("Amount:", response)
                unit_type = "kg"

            elif response.endswith('g'):
                print("Amount:", response)
                unit_type = "g"

            elif response.endswith('ml'):
                print("Amount:", response)
                unit_type = "ml"

            elif response:
                unit_type = "unknown"
            # asks question again if response invalid
            else:
                print(error)
                continue

            try:
                # Convert the amount to float
                amount = float(response[:-2])
                # Check if the amount is more than zero
                if amount <= 0:
                    print(error)
                    continue  # Added to restart the loop if the amount is not positive
                else:
                    break
            except ValueError:
                print(error)
                continue

            if unit_type == "unknown" and amount < 10:
                print(error)


# Call the measurement function
measurement()
