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
            return amount

        if unit_type == "g" or unit_type == "kg" or unit_type == "ml":
            return amount


def unit_converter(amount, unit_type):
    if unit_type == "kg":
        converted_amount = amount * 1000
        return converted_amount
    elif unit_type == "g":
        converted_amount = amount
        return amount
    elif unit_type == "ml":
        converted_amount = amount * 1000
        # Add conversion logic for milliliters here if needed
        return converted_amount
    else:
        # Handle other unit types here
        return amount


# Main routine goes here

while True:
    ingredient_amount = measurement("\nAmount of ingredient?: (e.g., 2kg, 200g, 20mL, or "
                                    "enter number with no unit): ")
    if ingredient_amount is None:
        break
    print("Ingredient amount:", ingredient_amount)

    converted_amount = unit_converter(ingredient_amount, "g")
    print("Converted amount:", converted_amount)
