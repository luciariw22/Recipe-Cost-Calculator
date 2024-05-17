def yes_no(question):
    to_check = ["yes", "no"]
    valid = False
    while not valid:
        response = input(question).lower()
        if response in to_check:
            return response
        else:
            print("Please enter either yes or no...\n")


def measurement(question):
    error = "Please enter a valid measurement\n"
    valid = False

    while not valid:
        response = input(question).lower()
        if response == "xxx":
            return None

        if response.endswith('kg'):
            print("Amount:", response)
            unit_type = "kg"

        elif response.endswith('g'):
            if response[:-1].isdigit():
                print("Amount:", response)
                unit_type = "g"
            else:
                print(error)
                continue

        elif response.endswith('ml'):
            print("Amount:", response)
            unit_type = "ml"

        else:
            unit_type = response

        try:
            if unit_type == "g":
                amount = float(response[:-1])
            elif unit_type == "kg" or unit_type == "ml":
                amount = float(response[:-2])
            else:
                amount = float(response)

            if amount <= 0:
                print("Please enter a valid amount")
                continue
            else:
                valid = True
        except ValueError:
            print(error)
            continue

        if unit_type == response:
            print("Amount:", response)
            # If no unit is entered, return the amount directly
            return amount, None

        return amount, unit_type


# Main routine goes here

while True:
    ingredient_amount, unit = measurement("\nAmount of ingredient needed for recipe?: (e.g., 2kg, 200g, "
                                          "20mL, or enter number with no unit): ")
    if ingredient_amount is None:
        break

    if unit == "kg":
        converted_amount = ingredient_amount * 1000
    elif unit == "ml":
        converted_amount = ingredient_amount
    else:
        converted_amount = ingredient_amount

    print("Converted amount:", converted_amount, "g" if unit is not None else "")
